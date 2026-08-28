const express = require('express');
const cors = require('cors');
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode');

const app = express();
app.use(cors());
app.use(express.json());

let clientStatus = 'INITIALIZING';
let qrCodeBase64 = null;
let reconnectTimer = null;

// Initialize WhatsApp Client with local authentication (saves session)
const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { 
        headless: true,
        args: [
            '--no-sandbox', 
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-accelerated-2d-canvas',
            '--no-first-run',
            '--no-zygote',
            '--single-process',
            '--disable-gpu'
        ]
    }
});

// Event: QR Code generated (User needs to scan)
client.on('qr', async (qr) => {
    clientStatus = 'WAITING_QR';
    try {
        qrCodeBase64 = await qrcode.toDataURL(qr);
        console.log('\n[!] NOVO QR CODE GERADO. Aguardando leitura no CRM...');
    } catch (err) {
        console.error('Erro ao gerar base64 do QR code:', err);
    }
});

// Event: WhatsApp Connected & Ready
client.on('ready', () => {
    clientStatus = 'CONNECTED';
    qrCodeBase64 = null;
    console.log('\n[✔] WhatsApp Conectado e Pronto para uso!');
});

// Event: WhatsApp Disconnected (User logged out from phone or connection lost)
client.on('disconnected', (reason) => {
    console.log('\n[X] WhatsApp Desconectado:', reason);
    clientStatus = 'DISCONNECTED';
    qrCodeBase64 = null;
    
    // Auto-reconnect after 5 seconds
    if (reconnectTimer) clearTimeout(reconnectTimer);
    reconnectTimer = setTimeout(() => {
        console.log('Reiniciando cliente WhatsApp...');
        clientStatus = 'INITIALIZING';
        client.initialize();
    }, 5000);
});

// Event: Auth failure
client.on('auth_failure', msg => {
    console.error('\n[X] Falha de autenticação:', msg);
    clientStatus = 'DISCONNECTED';
    qrCodeBase64 = null;
});

// --- API ENDPOINTS ---

// 1. Get Status & QR Code
app.get('/api/status', (req, res) => {
    res.json({
        status: clientStatus,
        qrCode: qrCodeBase64
    });
});

// 2. Send Message
app.post('/api/send', async (req, res) => {
    const { phone, message } = req.body;
    
    if (clientStatus !== 'CONNECTED') {
        return res.status(400).json({ error: 'WhatsApp não está conectado. Escaneie o QR Code primeiro.' });
    }
    
    if (!phone || !message) {
        return res.status(400).json({ error: 'Telefone e mensagem são obrigatórios.' });
    }

    try {
        // Format phone: must end with @c.us for regular contacts
        // Assuming phone comes as 5511999999999
        const cleanPhone = phone.replace(/\D/g, '');
        const chatId = `${cleanPhone}@c.us`;
        
        console.log(`[>>] Enviando mensagem para ${cleanPhone}...`);
        await client.sendMessage(chatId, message);
        console.log(`[OK] Mensagem enviada para ${cleanPhone}`);
        
        res.json({ success: true });
    } catch (error) {
        console.error('[ERRO] Falha ao enviar mensagem:', error);
        res.status(500).json({ error: error.message });
    }
});

// 3. Logout (Force disconnect)
app.post('/api/logout', async (req, res) => {
    try {
        if (clientStatus === 'CONNECTED') {
            await client.logout();
        }
        clientStatus = 'DISCONNECTED';
        qrCodeBase64 = null;
        res.json({ success: true });
        
        // Restart after logout
        setTimeout(() => client.initialize(), 2000);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start Server
const PORT = process.env.PORT || 3001;
app.listen(PORT, async () => {
    console.log(`=========================================`);
    console.log(`🚀 Microsserviço WhatsApp rodando localmente na porta ${PORT}`);
    
    // Create HTTPS tunnel so Vercel can access it
    try {
        const localtunnel = require('localtunnel');
        const tunnel = await localtunnel({ port: PORT });
        console.log(`\n✅ URL PÚBLICA (COLE ISSO NO UNICOCRM DA VERCEL):`);
        console.log(`➡️  ${tunnel.url}  ⬅️`);
        console.log(`=========================================\n`);
        
        tunnel.on('close', () => {
            console.log('Túnel fechado.');
        });
    } catch (err) {
        console.log('Erro ao criar túnel HTTPS:', err);
    }

    console.log('Inicializando cliente WhatsApp. Aguarde...');
    client.initialize().catch(err => {
        console.error('Erro fatal ao iniciar WhatsApp:', err);
    });
});

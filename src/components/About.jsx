import { motion } from 'framer-motion';

export default function About() {
  return (
    <section id="about" className="py-24 px-6 md:px-12 max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-100px' }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="section-heading">
          <span className="num">01.</span> Sobre mim
        </h2>

        <div className="grid md:grid-cols-3 gap-12">
          <div className="md:col-span-2 space-y-4">
            <p>
              Me chamo Filipe, tenho formação em{' '}
              <span className="text-lightest-slate">Ciência da Computação</span> (Descomplica, 2026) e{' '}
              <span className="text-lightest-slate">Design Gráfico</span> (Uninove, 2020).
              No dia a dia, transito entre código e suporte — já corrigi integrações
              quebradas de API às 23h e já redesenhei telas inteiras pensando em quem
              ia usar no celular.
            </p>
            <p>
              Hoje atuo na <span className="text-lightest-slate">Unico Drop</span> com
              suporte técnico N1/N2, integrações via API e Webhook,
              automações de fluxo (WhatsApp, e-mail), além de mexer no front
              com React quando precisa. Também monto dashboards em Power BI
              pra ajudar o time a tomar decisões com dados.
            </p>
            <p>
              Antes disso, passei pela <span className="text-lightest-slate">Levlife</span> como
              designer e social media, cuidando do e-commerce e criando conteúdo
              digital. E no <span className="text-lightest-slate">Cartório de São Caetano</span>,
              aprendi a lidar com volume alto de documentos e processos que não podem atrasar.
            </p>
            <p>
              Sou autodidata por natureza — quando não sei algo, vou atrás até resolver.
              Gosto de ambientes onde posso aprender rápido e contribuir de verdade.
            </p>
          </div>

          {/* Contact Info Card */}
          <div className="relative">
            <div className="bg-navy-light rounded-lg p-6 border border-navy-lighter/50">
              <h3 className="text-lightest-slate font-semibold text-lg mb-4">Contato</h3>
              <ul className="space-y-3 text-sm">
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Localização</span>
                    <span className="text-lightest-slate">São Caetano do Sul, SP</span>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Email</span>
                    <a href="mailto:filipe_vicente@hotmail.com" className="text-lightest-slate hover:text-teal transition-colors">
                      filipe_vicente@hotmail.com
                    </a>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Telefone / WhatsApp</span>
                    <span className="text-lightest-slate">(11) 96615-2956</span>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">LinkedIn</span>
                    <a href="https://www.linkedin.com/in/filipevicentehidalgo" target="_blank" rel="noreferrer" className="text-lightest-slate hover:text-teal transition-colors break-all">
                      linkedin.com/in/filipevicentehidalgo
                    </a>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Behance</span>
                    <a href="https://www.behance.net/filipevicenteh" target="_blank" rel="noreferrer" className="text-lightest-slate hover:text-teal transition-colors">
                      behance.net/filipevicenteh
                    </a>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">GitHub</span>
                    <a href="https://github.com/FilipeVicenteH" target="_blank" rel="noreferrer" className="text-lightest-slate hover:text-teal transition-colors">
                      github.com/FilipeVicenteH
                    </a>
                  </div>
                </li>
              </ul>
            </div>
            {/* Decorative offset border */}
            <div className="absolute -z-10 top-3 left-3 w-full h-full border border-teal/30 rounded-lg"></div>
          </div>
        </div>
      </motion.div>
    </section>
  );
}

import { useState } from 'react';
import { motion } from 'framer-motion';

const projects = [
  {
    title: 'UnicoCRM — Gestão de Retenção & Clientes Cancelados',
    subtitle: 'Sistema SaaS Completo de CRM e Reconversão de Churn em Tempo Real',
    images: [
      { url: '/projects/unicocrm_real.jpg', label: 'Visão Geral, Funil & Métricas de Churn' },
      { url: '/projects/unicocrm_clientes_real.jpg', label: 'Gestão & Lista de Clientes Cancelados' }
    ],
    challenge: 'A falta de um sistema centralizado e automatizado para gerenciar solicitações de cancelamento na plataforma UnicoDrop gerava perda contínua de histórico operacional, atraso no contato da equipe de suporte/CS e imprecisão na identificação dos reais motivos de churn da base de lojistas.',
    solution: 'Idealização e desenvolvimento completo de uma aplicação SaaS Full Stack do zero utilizando Next.js 15 (App Router e Server Actions), TypeScript, banco de dados Serverless Neon PostgreSQL com ORM Prisma, estilização responsiva com Tailwind CSS e dashboards de indicadores com Recharts. O sistema conta com filtros avançados por período, status de negociação (Convertido, Em Negociação, Pendente, Inacessível), prioridade de atendimento e integração de notificações.',
    result: 'Estruturação e padronização do processo de suporte e reconversão de cancelamentos, elevando a transparência das operações em tempo real, permitindo a recuperação ativa de clientes e fornecendo à gestão dados precisos para redução da taxa de churn.',
    tags: ['Next.js 15', 'TypeScript', 'Neon PostgreSQL', 'Prisma ORM', 'Tailwind CSS', 'Recharts', 'SaaS Full Stack'],
    github: 'https://github.com/FilipeVicenteH/UnicoDrop-Cancelados',
    demo: 'https://unico-crm.vercel.app/relatorios',
    featured: true,
  },
  {
    title: 'Redesign Visual de Interface — Plataforma UnicoDrop',
    subtitle: 'Página de Apresentação de Case Study UI/UX, Design System e Componentes Criados',
    images: [
      { url: '/projects/telas_ranking_real.jpg', label: 'Dashboard Executivo & Ranking de Produtos' },
      { url: '/projects/telas_rastreio_real.jpg', label: 'Módulo de Lista de Rastreio & Logística' }
    ],
    challenge: 'A interface legada da plataforma apresentava layout poluído, baixa hierarquia visual de informações críticas (como faturamento, custos e códigos de rastreio) e ausência de padronização em dispositivos móveis, gerando alta curva de aprendizado e insatisfação nos usuários.',
    solution: 'Prototipagem de alta fidelidade e reformulação do Design System no Figma focando na usabilidade do usuário e princípios modernos de UI/UX. Em seguida, recodificação completa do frontend utilizando React e Tailwind CSS, criando componentes altamente reutilizáveis, tabelas interativas com DataTables, cartões de KPIs dinâmicos, filtros de período e modais de atualização de custos.',
    result: 'Navegação mais intuitiva e veloz, redução significativa do tempo que o lojista leva para visualizar métricas vitais da sua operação e aumento comprovado na satisfação estética e retenção dos usuários no sistema.',
    tags: ['React', 'JavaScript', 'Tailwind CSS', 'Figma', 'UI/UX Design', 'DataTables', 'Frontend SaaS'],
    github: 'https://github.com/FilipeVicenteH/Telas-Unico',
    demo: 'https://telas-unico.vercel.app',
    featured: true,
  },
  {
    title: 'Landing Page de Diagnóstico & Conversão — UnicoDrop',
    subtitle: 'Aplicação Web Interativa para Diagnóstico Operacional e Captação de Leads via Webhook',
    images: [
      { url: '/projects/landingshopify_real.jpg', label: 'Auditoria Gratuita em 7 Perguntas & Métricas' }
    ],
    challenge: 'Necessidade de captar novos lojistas de e-commerce e qualificar a dor do cliente (perda de vendas e abandono de checkout) antes do primeiro contato da equipe comercial de Customer Success e Vendas.',
    solution: 'Desenvolvimento de uma Landing Page focada em alta conversão com fluxo interativo de auditoria em 7 perguntas dinâmicas em menos de 3 minutos. Construída com HTML5 semântico, CSS3 moderno com gradientes e sombras sutis, JavaScript ES6+ assíncrono e integração direta com Webhooks HTTP para envio de respostas diretamente para sistemas de CRM/WhatsApp da empresa.',
    result: 'Transformação do processo de captação de leads em uma experiência de valor imediato para o cliente, permitindo qualificação automatizada de potenciais contas e aumento relevante nas taxas de conversão de novos usuários.',
    tags: ['JavaScript (ES6+)', 'HTML5', 'CSS3', 'Webhooks', 'UI/UX Design', 'Vercel', 'CRO & Landing Pages'],
    github: 'https://github.com/FilipeVicenteH/TesteWebHook',
    demo: 'https://teste-web-hook.vercel.app',
    featured: false,
  },
];

export default function Projects() {
  const [activeImageIndexes, setActiveImageIndexes] = useState({});

  const handleImageSwitch = (projIndex, imgIndex) => {
    setActiveImageIndexes(prev => ({ ...prev, [projIndex]: imgIndex }));
  };

  return (
    <section id="projects" className="py-24 px-6 md:px-12 max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-100px' }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="section-heading">
          <span className="num">03.</span> Projetos em Destaque
        </h2>

        <div className="space-y-14">
          {projects.map((proj, i) => {
            const currentImgIndex = activeImageIndexes[i] || 0;
            const currentImage = proj.images[currentImgIndex];

            return (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 25 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: i * 0.1 }}
                className="bg-navy-light rounded-xl border border-navy-lighter/40 hover:border-teal/40 transition-all duration-300 overflow-hidden shadow-xl"
              >
                {/* Top Browser Bar Mockup */}
                <div className="bg-navy-darker/80 px-4 py-3 border-b border-navy-lighter/30 flex items-center justify-between flex-wrap gap-2">
                  <div className="flex items-center gap-2">
                    <span className="w-3 h-3 rounded-full bg-red-500/80 inline-block"></span>
                    <span className="w-3 h-3 rounded-full bg-yellow-500/80 inline-block"></span>
                    <span className="w-3 h-3 rounded-full bg-green-500/80 inline-block"></span>
                    <span className="font-mono text-xs text-slate ml-2 hidden sm:inline-block">
                      {proj.title.split('—')[0].trim()}
                    </span>
                  </div>

                  {/* Multi-Image Tabs if project has multiple screenshots */}
                  {proj.images.length > 1 && (
                    <div className="flex items-center gap-1.5 bg-navy/60 p-1 rounded border border-navy-lighter/30">
                      {proj.images.map((img, idx) => (
                        <button
                          key={idx}
                          onClick={() => handleImageSwitch(i, idx)}
                          className={`px-2.5 py-1 text-[11px] font-mono rounded transition-all ${
                            currentImgIndex === idx
                              ? 'bg-teal text-navy-dark font-bold'
                              : 'text-slate hover:text-lightest-slate hover:bg-navy-lighter/40'
                          }`}
                        >
                          Tela {idx + 1}
                        </button>
                      ))}
                    </div>
                  )}

                  <div className="flex items-center gap-2 ml-auto sm:ml-0">
                    {proj.demo && (
                      <a
                        href={proj.demo}
                        target="_blank"
                        rel="noreferrer"
                        className="text-teal hover:bg-teal/10 transition-colors flex items-center gap-1.5 font-mono text-xs border border-teal/40 px-3 py-1 rounded bg-teal-tint/30"
                      >
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
                        </svg>
                        Ver no Vercel
                      </a>
                    )}
                    {proj.github && (
                      <a
                        href={proj.github}
                        target="_blank"
                        rel="noreferrer"
                        className="text-slate hover:text-teal transition-colors flex items-center gap-1.5 font-mono text-xs bg-navy-lighter/30 px-3 py-1 rounded hover:bg-navy-lighter/50"
                      >
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                          <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>
                          <path d="M9 18c-4.51 2-5-2-7-2"/>
                        </svg>
                        GitHub
                      </a>
                    )}
                  </div>
                </div>

                {/* Grid: Visual Screenshot Showcase + Detailed Project Info */}
                <div className="grid lg:grid-cols-12 gap-0">
                  {/* Visual Image Preview Frame */}
                  <div className="lg:col-span-5 relative overflow-hidden bg-navy-darker flex flex-col items-center justify-center group min-h-[260px]">
                    <img
                      key={currentImage.url}
                      src={currentImage.url}
                      alt={currentImage.label}
                      className="w-full h-full object-cover object-top max-h-[360px] lg:max-h-full group-hover:scale-105 transition-transform duration-500 opacity-95 group-hover:opacity-100"
                    />
                    {currentImage.label && (
                      <span className="absolute bottom-2 left-2 bg-navy-darker/90 text-teal font-mono text-[10px] px-2.5 py-1 rounded border border-teal/20 backdrop-blur-sm">
                        📷 {currentImage.label}
                      </span>
                    )}
                  </div>

                  {/* Deep Project Details */}
                  <div className="lg:col-span-7 p-6 md:p-8 flex flex-col justify-between">
                    <div>
                      <h3 className="text-lightest-slate text-xl font-bold mb-1 leading-snug">{proj.title}</h3>
                      <p className="text-teal font-mono text-xs mb-4">{proj.subtitle}</p>

                      {/* Expanded Challenge, Solution, Result Sections */}
                      <div className="space-y-3.5 text-xs mb-5">
                        <div className="bg-navy/50 p-3.5 rounded-lg border border-navy-lighter/20">
                          <span className="text-teal font-mono font-semibold block mb-1">🎯 Desafio de Negócio:</span>
                          <p className="text-slate leading-relaxed">{proj.challenge}</p>
                        </div>

                        <div className="bg-navy/50 p-3.5 rounded-lg border border-navy-lighter/20">
                          <span className="text-teal font-mono font-semibold block mb-1">💻 Arquitetura & Solução Técnica:</span>
                          <p className="text-slate leading-relaxed">{proj.solution}</p>
                        </div>

                        <div className="bg-teal/10 p-3.5 rounded-lg border border-teal/20">
                          <span className="text-teal font-mono font-semibold block mb-1">📈 Impacto & Resultados Obtidos:</span>
                          <p className="text-lightest-slate leading-relaxed font-medium">{proj.result}</p>
                        </div>
                      </div>
                    </div>

                    {/* Tech Badges */}
                    <div className="flex flex-wrap gap-1.5 pt-2">
                      {proj.tags.map((tag, j) => (
                        <span
                          key={j}
                          className="px-2.5 py-0.5 text-xs font-mono text-teal bg-teal-tint rounded-full border border-teal/20"
                        >
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </div>
      </motion.div>
    </section>
  );
}

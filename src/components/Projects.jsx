import { useState } from 'react';
import { motion } from 'framer-motion';

const projects = [
  {
    title: 'UnicoCRM — Gestão de Retenção & Clientes Cancelados',
    subtitle: 'Sistema CRM para Acompanhamento e Reconversão de Churn',
    images: [
      { url: '/projects/unicocrm.jpg', label: 'Visão Geral & Métricas de Churn' },
      { url: '/projects/unicocrm_clientes_real.jpg', label: 'Lista de Clientes Cancelados' }
    ],
    challenge: 'Falta de um fluxo centralizado para acompanhar clientes cancelados do UnicoDrop, gerando perda de histórico e dificultando ações de retenção.',
    solution: 'Desenvolvimento de um sistema CRM completo do zero utilizando Next.js 15 (App Router + TypeScript), ORM Prisma, banco de dados Serverless Neon PostgreSQL e dashboards de métricas com Recharts.',
    result: 'Estruturação do processo de acompanhamento de cancelamentos em tempo real, permitindo identificar motivos de churn e executar estratégias diretas de reconversão de clientes.',
    tags: ['Next.js 15', 'TypeScript', 'Neon PostgreSQL', 'Prisma ORM', 'Tailwind CSS', 'Recharts'],
    github: 'https://github.com/FilipeVicenteH/UnicoDrop-Cancelados',
    featured: true,
  },
  {
    title: 'Redesign Visual de Interface — Plataforma UnicoDrop',
    subtitle: 'Reformulação Completa de UI/UX e Frontend da Aplicação',
    images: [
      { url: '/projects/telasunico.jpg', label: 'Dashboard & Ranking de Produtos' },
      { url: '/projects/telasunico_2.jpg', label: 'Lista de Rastreio & Logística' }
    ],
    challenge: 'Interface do usuário necessitava de modernização estética e estrutural para melhorar a usabilidade e a taxa de retenção dos clientes na plataforma.',
    solution: 'Prototipagem de telas no Figma focando na usabilidade (UI/UX) e recodificação completa dos componentes visuais utilizando React e Tailwind CSS.',
    result: 'Interface responsiva, limpa e alinhada aos padrões modernos de software SaaS, reduzindo o atrito na navegação do usuário final e aumentando a satisfação visual.',
    tags: ['React', 'JavaScript', 'Tailwind CSS', 'Figma', 'UI/UX Design'],
    github: 'https://github.com/FilipeVicenteH/Telas-Unico',
    featured: true,
  },
  {
    title: 'Painel & Análise de Dados Operacionais',
    subtitle: 'Dashboards Integrados de Atendimento e Métricas de TI',
    images: [
      { url: '/projects/painelunico.jpg', label: 'Visão Geral de Desempenho & SLAs' }
    ],
    challenge: 'Ausência de visão consolidada sobre volume de chamados N1/N2, tempo de atendimento (SLA) e recorrência de incidentes técnicos.',
    solution: 'Construção de painel gerencial em React integrado com dashboards interativos em Power BI para monitoramento de dados operacionais.',
    result: 'Tomada de decisão baseada em dados reais pela gestão, acelerando o diagnóstico de falhas em integrações e a eficiência no suporte técnico.',
    tags: ['Power BI', 'React', 'SQL', 'Excel Intermediário', 'APIs'],
    github: 'https://github.com/FilipeVicenteH/PainelUnico',
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

        <div className="space-y-12">
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

                  {proj.github && (
                    <a
                      href={proj.github}
                      target="_blank"
                      rel="noreferrer"
                      className="text-slate hover:text-teal transition-colors flex items-center gap-1.5 font-mono text-xs bg-navy-lighter/30 px-3 py-1 rounded hover:bg-navy-lighter/50 ml-auto sm:ml-0"
                    >
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>
                        <path d="M9 18c-4.51 2-5-2-7-2"/>
                      </svg>
                      Ver no GitHub
                    </a>
                  )}
                </div>

                {/* Grid: Visual Screenshot Showcase + Project Details */}
                <div className="grid lg:grid-cols-12 gap-0">
                  {/* Visual Image Preview Frame */}
                  <div className="lg:col-span-5 relative overflow-hidden bg-navy-darker flex flex-col items-center justify-center group min-h-[240px]">
                    <img
                      key={currentImage.url}
                      src={currentImage.url}
                      alt={currentImage.label}
                      className="w-full h-full object-cover object-top max-h-[320px] lg:max-h-full group-hover:scale-105 transition-transform duration-500 opacity-95 group-hover:opacity-100"
                    />
                    {currentImage.label && (
                      <span className="absolute bottom-2 left-2 bg-navy-darker/90 text-teal font-mono text-[10px] px-2.5 py-1 rounded border border-teal/20 backdrop-blur-sm">
                        📷 {currentImage.label}
                      </span>
                    )}
                  </div>

                  {/* Project Context & Details */}
                  <div className="lg:col-span-7 p-6 md:p-8 flex flex-col justify-between">
                    <div>
                      <h3 className="text-lightest-slate text-xl font-bold mb-1">{proj.title}</h3>
                      <p className="text-teal font-mono text-xs mb-4">{proj.subtitle}</p>

                      {/* Challenge, Solution, Result Pills */}
                      <div className="space-y-3 text-xs mb-5">
                        <div className="bg-navy/50 p-3 rounded border border-navy-lighter/20">
                          <span className="text-teal font-mono font-semibold block mb-0.5">🎯 Desafio:</span>
                          <p className="text-slate leading-relaxed">{proj.challenge}</p>
                        </div>

                        <div className="bg-navy/50 p-3 rounded border border-navy-lighter/20">
                          <span className="text-teal font-mono font-semibold block mb-0.5">💻 Solução Técnica:</span>
                          <p className="text-slate leading-relaxed">{proj.solution}</p>
                        </div>

                        <div className="bg-teal/10 p-3 rounded border border-teal/20">
                          <span className="text-teal font-mono font-semibold block mb-0.5">📈 Resultado de Negócio:</span>
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

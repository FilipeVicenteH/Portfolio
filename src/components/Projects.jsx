import { useState } from 'react';
import { motion } from 'framer-motion';

const projects = [
  {
    number: '01',
    title: 'UnicoCRM',
    subtitle: 'Gestão de Retenção & Reconversão de Churn',
    architecture: 'Desenvolvi do zero uma aplicação SaaS Full Stack em Next.js 15 (App Router e Server Actions), TypeScript e Tailwind CSS, integrada a um banco de dados Serverless Neon PostgreSQL via Prisma ORM. O projeto nasceu da necessidade de centralizar o atendimento a solicitações de cancelamento na UnicoDrop, organizando o histórico de interações, categorização por motivo de saída (preço, suporte, bugs, concorrência) e filtros por status de negociação e prioridade.',
    impact: 'O sistema automatizou a régua de retenção de clientes, permitindo que a equipe de Customer Success atuasse proativamente na reconversão de lojistas antes da perda definitiva, gerando impacto direto na redução da taxa de churn e preservação de receita recorrente (MRR).',
    tech: ['Next.js 15', 'TypeScript', 'Neon PostgreSQL', 'Prisma ORM', 'Tailwind CSS', 'Recharts', 'SaaS Full Stack'],
    images: [
      { url: '/projects/unicocrm_real.jpg', label: 'Visão Geral & Funil de Churn' },
      { url: '/projects/unicocrm_clientes_real.jpg', label: 'Lista de Clientes Cancelados' },
    ],
    github: 'https://github.com/FilipeVicenteH/UnicoDrop-Cancelados',
    demo: 'https://unico-crm.vercel.app/relatorios',
    type: 'SaaS Full Stack',
  },
  {
    number: '02',
    title: 'UnicoDrop Redesign',
    subtitle: '30 Interfaces Codadas — Case Study UI/UX',
    architecture: 'Liderei a reformulação estética e funcional da plataforma UnicoDrop, desde a prototipagem de alta fidelidade e estruturação do Design System no Figma até a recodificação completa de 30 interfaces operacionais em React, Tailwind CSS e ApexCharts. O layout legado sofria com poluição visual e baixa hierarquia de dados; a nova arquitetura organizou métricas financeiras (DRE, faturamento), rastreio logístico e automações de mensageria em 4 módulos coesos.',
    impact: 'A nova interface simplificou a curva de aprendizado dos usuários, proporcionando redução estimada em 40% no tempo necessário para consultar informações operacionais críticas e elevando o nível de satisfação estética e retenção na plataforma.',
    tech: ['React', 'JavaScript', 'Tailwind CSS', 'Figma', 'ApexCharts', 'DataTables', 'Frontend SaaS'],
    images: [
      { url: '/projects/telas_ranking_real.jpg', label: 'Dashboard Executivo & Ranking' },
      { url: '/projects/telas_rastreio_real.jpg', label: 'Módulo de Rastreio & Logística' },
    ],
    github: 'https://github.com/FilipeVicenteH/Telas-Unico',
    demo: 'https://telas-unico.vercel.app',
    type: 'UI/UX & Frontend',
  },
  {
    number: '03',
    title: 'Diagnóstico UnicoDrop',
    subtitle: 'Landing Page de Captação via Webhook',
    architecture: 'Projetei e codifiquei uma landing page interativa focada na captação e qualificação automatizada de leads para a UnicoDrop. Desenvolvida com HTML5 semântico, CSS3 e JavaScript ES6+ assíncrono, a página guia o visitante por um fluxo de auditoria operacional em 7 perguntas dinâmicas (avaliação de vendas, frete e checkout) e dispara os dados de qualificação em tempo real via Webhooks HTTP diretamente para os sistemas de vendas/CRM.',
    impact: 'Eliminou a necessidade de triagem manual inicial pela equipe comercial, entregando um diagnóstico instantâneo de alto valor ao lojista e aumentando expressivamente a taxa de conversão de novos e-commerces qualificados.',
    tech: ['JavaScript ES6+', 'HTML5', 'CSS3', 'Webhooks HTTP', 'Vercel', 'CRO & Landing Pages'],
    images: [
      { url: '/projects/landingshopify_real.jpg', label: 'Auditoria em 7 Perguntas' },
    ],
    github: 'https://github.com/FilipeVicenteH/TesteWebHook',
    demo: 'https://teste-web-hook.vercel.app',
    type: 'Frontend & Integração',
  },
];

// Icons
const IconExternal = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
    <polyline points="15 3 21 3 21 9"/>
    <line x1="10" y1="14" x2="21" y2="3"/>
  </svg>
);

const IconGithub = () => (
  <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>
    <path d="M9 18c-4.51 2-5-2-7-2"/>
  </svg>
);

export default function Projects() {
  const [activeImageIndexes, setActiveImageIndexes] = useState({});
  const [hoveredProject, setHoveredProject] = useState(null);

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
              <motion.article
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: i * 0.08 }}
                onMouseEnter={() => setHoveredProject(i)}
                onMouseLeave={() => setHoveredProject(null)}
                className="group relative rounded-2xl overflow-hidden transition-all duration-500"
                style={{
                  background: 'rgba(23, 42, 69, 0.5)',
                  border: hoveredProject === i ? '1px solid rgba(13,148,136,0.35)' : '1px solid rgba(255,255,255,0.06)',
                  boxShadow: hoveredProject === i
                    ? '0 0 0 1px rgba(13,148,136,0.1), 0 24px 48px rgba(0,0,0,0.3)'
                    : '0 4px 24px rgba(0,0,0,0.2)',
                }}
              >
                <div className="grid lg:grid-cols-12 gap-0 min-h-[380px]">

                  {/* — Left: Image Showcase — */}
                  <div className="lg:col-span-5 relative overflow-hidden bg-[#0a1628] min-h-[280px] lg:min-h-full flex flex-col justify-between">
                    <img
                      key={currentImage.url}
                      src={currentImage.url}
                      alt={currentImage.label}
                      className="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-[1.03]"
                      style={{ opacity: 0.92 }}
                    />

                    {/* Gradient overlay bottom for caption & dots */}
                    <div className="absolute inset-0 bg-gradient-to-t from-[#0a1628] via-transparent to-transparent pointer-events-none opacity-80" />

                    {/* Type badge top-left */}
                    <div className="absolute top-4 left-4">
                      <span
                        className="text-[10px] font-mono tracking-widest uppercase px-2.5 py-1 rounded"
                        style={{
                          background: 'rgba(13,148,136,0.15)',
                          color: '#0D9488',
                          border: '1px solid rgba(13,148,136,0.25)',
                          backdropFilter: 'blur(8px)',
                        }}
                      >
                        {proj.type}
                      </span>
                    </div>

                    {/* Image switcher dots & Caption — bottom */}
                    <div className="absolute bottom-4 left-4 right-4 flex items-center justify-between gap-2">
                      <span className="text-[11px] font-mono text-slate-light/80 truncate">
                        {currentImage.label}
                      </span>

                      {proj.images.length > 1 && (
                        <div className="flex items-center gap-1.5 shrink-0 bg-[#0a1628]/80 p-1 rounded-full border border-white/10 backdrop-blur-sm">
                          {proj.images.map((img, idx) => (
                            <button
                              key={idx}
                              onClick={() => handleImageSwitch(i, idx)}
                              title={img.label}
                              className="transition-all duration-200 rounded-full focus:outline-none"
                              style={{
                                width: currentImgIndex === idx ? '20px' : '6px',
                                height: '6px',
                                background: currentImgIndex === idx ? '#0D9488' : 'rgba(255,255,255,0.3)',
                              }}
                            />
                          ))}
                        </div>
                      )}
                    </div>
                  </div>

                  {/* — Right: Detailed Content Panel — */}
                  <div className="lg:col-span-7 flex flex-col justify-between p-6 md:p-8">

                    {/* Header */}
                    <div>
                      {/* Number + title row */}
                      <div className="flex items-start gap-3.5 mb-3">
                        <span
                          className="font-mono text-3xl md:text-4xl font-bold leading-none select-none mt-0.5"
                          style={{
                            color: 'transparent',
                            WebkitTextStroke: '1px rgba(13,148,136,0.35)',
                          }}
                        >
                          {proj.number}
                        </span>
                        <div>
                          <h3
                            className="text-lg md:text-xl font-bold leading-snug transition-colors duration-300"
                            style={{ color: hoveredProject === i ? '#F1F5F9' : '#CBD5E1' }}
                          >
                            {proj.title}
                          </h3>
                          <p className="text-xs md:text-sm font-mono" style={{ color: '#0D9488' }}>
                            {proj.subtitle}
                          </p>
                        </div>
                      </div>

                      {/* Divider */}
                      <div
                        className="mb-4 transition-all duration-500"
                        style={{
                          height: '1px',
                          background: hoveredProject === i
                            ? 'linear-gradient(90deg, rgba(13,148,136,0.5) 0%, transparent 100%)'
                            : 'rgba(255,255,255,0.06)',
                        }}
                      />

                      {/* Architecture & Challenge Detailed Text */}
                      <p
                        className="text-xs md:text-sm leading-relaxed mb-4"
                        style={{ color: '#94A3B8' }}
                      >
                        {proj.architecture}
                      </p>

                      {/* Business Impact Highlight Block */}
                      <div
                        className="mb-5 p-3.5 rounded-r-lg border-l-2 transition-all duration-300"
                        style={{
                          background: 'rgba(13,148,136,0.06)',
                          borderColor: '#0D9488',
                        }}
                      >
                        <span className="text-[11px] font-mono uppercase tracking-wider block mb-1 font-semibold" style={{ color: '#0D9488' }}>
                          Impacto & Resultado Prático
                        </span>
                        <p className="text-xs leading-relaxed" style={{ color: '#E2E8F0' }}>
                          {proj.impact}
                        </p>
                      </div>

                      {/* Tech tags */}
                      <div className="flex flex-wrap gap-1.5 mb-5">
                        {proj.tech.map((tag, j) => (
                          <span
                            key={j}
                            className="text-[11px] font-mono px-2.5 py-0.5 rounded-full"
                            style={{
                              color: '#94A3B8',
                              background: 'rgba(255,255,255,0.04)',
                              border: '1px solid rgba(255,255,255,0.08)',
                            }}
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    </div>

                    {/* Action Links */}
                    <div className="flex items-center gap-3 pt-2">
                      {proj.demo && (
                        <a
                          href={proj.demo}
                          target="_blank"
                          rel="noreferrer"
                          className="flex items-center gap-2 text-xs md:text-sm font-medium px-4 py-2 rounded-lg transition-all duration-200"
                          style={{
                            color: '#0D9488',
                            background: 'rgba(13,148,136,0.12)',
                            border: '1px solid rgba(13,148,136,0.3)',
                          }}
                          onMouseEnter={e => {
                            e.currentTarget.style.background = 'rgba(13,148,136,0.22)';
                            e.currentTarget.style.borderColor = 'rgba(13,148,136,0.6)';
                          }}
                          onMouseLeave={e => {
                            e.currentTarget.style.background = 'rgba(13,148,136,0.12)';
                            e.currentTarget.style.borderColor = 'rgba(13,148,136,0.3)';
                          }}
                        >
                          <IconExternal />
                          Ver projeto
                        </a>
                      )}
                      {proj.github && (
                        <a
                          href={proj.github}
                          target="_blank"
                          rel="noreferrer"
                          className="flex items-center gap-2 text-xs md:text-sm px-4 py-2 rounded-lg transition-all duration-200"
                          style={{
                            color: '#94A3B8',
                            background: 'rgba(255,255,255,0.03)',
                            border: '1px solid rgba(255,255,255,0.08)',
                          }}
                          onMouseEnter={e => {
                            e.currentTarget.style.color = '#E2E8F0';
                            e.currentTarget.style.borderColor = 'rgba(255,255,255,0.2)';
                            e.currentTarget.style.background = 'rgba(255,255,255,0.07)';
                          }}
                          onMouseLeave={e => {
                            e.currentTarget.style.color = '#94A3B8';
                            e.currentTarget.style.borderColor = 'rgba(255,255,255,0.08)';
                            e.currentTarget.style.background = 'rgba(255,255,255,0.03)';
                          }}
                        >
                          <IconGithub />
                          GitHub
                        </a>
                      )}
                    </div>
                  </div>
                </div>
              </motion.article>
            );
          })}
        </div>
      </motion.div>
    </section>
  );
}

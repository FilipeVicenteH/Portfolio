import { useState } from 'react';
import { motion } from 'framer-motion';

const projects = [
  {
    number: '01',
    title: 'UnicoCRM',
    subtitle: 'Gestão de Retenção & Reconversão de Churn',
    description: 'Construí do zero uma aplicação SaaS Full Stack para centralizar o processo de cancelamentos da UnicoDrop. O sistema reúne histórico de interações, categoriza motivos de churn e acompanha o pipeline de reativação — tudo em tempo real.',
    tech: ['Next.js 15', 'TypeScript', 'Neon PostgreSQL', 'Prisma ORM', 'Tailwind CSS', 'Recharts'],
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
    description: 'Reformulei a interface legada da plataforma UnicoDrop — desde a prototipagem no Figma até a recodificação de 30 telas em React. O novo Design System organizou dashboards, tabelas de pedidos, módulos de logística e automações em uma experiência coesa.',
    tech: ['React', 'JavaScript', 'Tailwind CSS', 'Figma', 'ApexCharts', 'DataTables'],
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
    description: 'Desenvolvi uma landing page de alta conversão com fluxo interativo em 7 perguntas para qualificar lojistas antes do contato comercial. Os dados são enviados em tempo real para o CRM via Webhooks HTTP, eliminando a triagem manual pela equipe.',
    tech: ['JavaScript ES6+', 'HTML5', 'CSS3', 'Webhooks HTTP', 'Vercel'],
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

        <div className="space-y-6">
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
                <div className="grid lg:grid-cols-2 gap-0 min-h-[340px]">

                  {/* — Left: Image Panel — */}
                  <div className="relative overflow-hidden bg-[#0a1628] min-h-[260px] lg:min-h-full">
                    <img
                      key={currentImage.url}
                      src={currentImage.url}
                      alt={currentImage.label}
                      className="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-[1.03]"
                      style={{ opacity: 0.9 }}
                    />

                    {/* Gradient overlay bottom-left for caption */}
                    <div className="absolute inset-0 bg-gradient-to-t from-[#0a1628]/80 via-transparent to-transparent pointer-events-none" />

                    {/* Image switcher dots — only if multiple images */}
                    {proj.images.length > 1 && (
                      <div className="absolute bottom-4 left-4 flex items-center gap-2">
                        {proj.images.map((img, idx) => (
                          <button
                            key={idx}
                            onClick={() => handleImageSwitch(i, idx)}
                            title={img.label}
                            className="transition-all duration-200 rounded-full focus:outline-none"
                            style={{
                              width: currentImgIndex === idx ? '24px' : '8px',
                              height: '8px',
                              background: currentImgIndex === idx ? 'rgba(13,148,136,1)' : 'rgba(255,255,255,0.3)',
                            }}
                          />
                        ))}
                      </div>
                    )}

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
                  </div>

                  {/* — Right: Content Panel — */}
                  <div className="flex flex-col justify-between p-7 md:p-9">

                    {/* Header */}
                    <div>
                      {/* Number + title row */}
                      <div className="flex items-start gap-4 mb-4">
                        <span
                          className="font-mono text-4xl font-bold leading-none select-none mt-0.5"
                          style={{
                            color: 'transparent',
                            WebkitTextStroke: '1px rgba(13,148,136,0.3)',
                          }}
                        >
                          {proj.number}
                        </span>
                        <div>
                          <h3
                            className="text-lg font-bold leading-tight mb-0.5 transition-colors duration-300"
                            style={{ color: hoveredProject === i ? '#E2E8F0' : '#CBD5E1' }}
                          >
                            {proj.title}
                          </h3>
                          <p className="text-sm" style={{ color: '#0D9488' }}>
                            {proj.subtitle}
                          </p>
                        </div>
                      </div>

                      {/* Divider */}
                      <div
                        className="mb-5 transition-all duration-500"
                        style={{
                          height: '1px',
                          background: hoveredProject === i
                            ? 'linear-gradient(90deg, rgba(13,148,136,0.5) 0%, transparent 100%)'
                            : 'rgba(255,255,255,0.06)',
                        }}
                      />

                      {/* Description — plain prose, no boxes */}
                      <p
                        className="text-sm leading-relaxed mb-6"
                        style={{ color: '#8892B0' }}
                      >
                        {proj.description}
                      </p>

                      {/* Tech tags — minimal pill style */}
                      <div className="flex flex-wrap gap-2 mb-6">
                        {proj.tech.map((tag, j) => (
                          <span
                            key={j}
                            className="text-[11px] font-mono px-2.5 py-0.5 rounded-full"
                            style={{
                              color: '#64748B',
                              background: 'rgba(255,255,255,0.04)',
                              border: '1px solid rgba(255,255,255,0.08)',
                            }}
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    </div>

                    {/* Footer: Links */}
                    <div className="flex items-center gap-3">
                      {proj.demo && (
                        <a
                          href={proj.demo}
                          target="_blank"
                          rel="noreferrer"
                          className="flex items-center gap-2 text-sm font-medium px-4 py-2 rounded-lg transition-all duration-200"
                          style={{
                            color: '#0D9488',
                            background: 'rgba(13,148,136,0.1)',
                            border: '1px solid rgba(13,148,136,0.25)',
                          }}
                          onMouseEnter={e => {
                            e.currentTarget.style.background = 'rgba(13,148,136,0.2)';
                            e.currentTarget.style.borderColor = 'rgba(13,148,136,0.5)';
                          }}
                          onMouseLeave={e => {
                            e.currentTarget.style.background = 'rgba(13,148,136,0.1)';
                            e.currentTarget.style.borderColor = 'rgba(13,148,136,0.25)';
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
                          className="flex items-center gap-2 text-sm px-4 py-2 rounded-lg transition-all duration-200"
                          style={{
                            color: '#64748B',
                            background: 'rgba(255,255,255,0.03)',
                            border: '1px solid rgba(255,255,255,0.07)',
                          }}
                          onMouseEnter={e => {
                            e.currentTarget.style.color = '#CBD5E1';
                            e.currentTarget.style.borderColor = 'rgba(255,255,255,0.15)';
                            e.currentTarget.style.background = 'rgba(255,255,255,0.06)';
                          }}
                          onMouseLeave={e => {
                            e.currentTarget.style.color = '#64748B';
                            e.currentTarget.style.borderColor = 'rgba(255,255,255,0.07)';
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

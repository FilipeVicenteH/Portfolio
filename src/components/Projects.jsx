import { motion } from 'framer-motion';

const projects = [
  {
    title: 'UnicoCRM — Gestão de Retenção & Clientes Cancelados',
    subtitle: 'Sistema CRM para Acompanhamento e Reconversão de Churn',
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
    challenge: 'Ausência de visão consolidada sobre volume de chamados N1/N2, tempo de atendimento (SLA) e recorrência de incidentes técnicos.',
    solution: 'Construção de painel gerencial em React integrado com dashboards interativos em Power BI para monitoramento de dados operacionais.',
    result: 'Tomada de decisão baseada em dados reais pela gestão, acelerando o diagnóstico de falhas em integrações e a eficiência no suporte técnico.',
    tags: ['Power BI', 'React', 'SQL', 'Excel Intermediário', 'APIs'],
    github: 'https://github.com/FilipeVicenteH/PainelUnico',
    featured: false,
  },
];

export default function Projects() {
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

        <div className="space-y-8">
          {projects.map((proj, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.4, delay: i * 0.1 }}
              className="bg-navy-light p-6 md:p-8 rounded-lg border border-navy-lighter/40 hover:border-teal/30 transition-all duration-300 relative group"
            >
              <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-2 mb-4">
                <div>
                  <h3 className="text-lightest-slate text-xl font-bold group-hover:text-teal transition-colors">
                    {proj.title}
                  </h3>
                  <p className="text-teal font-mono text-xs mt-1">{proj.subtitle}</p>
                </div>
                {proj.github && (
                  <a
                    href={proj.github}
                    target="_blank"
                    rel="noreferrer"
                    className="text-slate hover:text-teal transition-colors shrink-0 mt-2 md:mt-0 flex items-center gap-2 font-mono text-xs border border-navy-lighter px-3 py-1.5 rounded hover:border-teal/50"
                    aria-label="GitHub Repository"
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/>
                      <path d="M9 18c-4.51 2-5-2-7-2"/>
                    </svg>
                    Ver no GitHub
                  </a>
                )}
              </div>

              {/* Problem / Solution / Result Grid */}
              <div className="grid md:grid-cols-3 gap-4 my-5 bg-navy/60 p-4 rounded-md border border-navy-lighter/20 text-sm">
                <div>
                  <span className="text-teal font-mono text-xs uppercase tracking-wider block mb-1">
                    🎯 O Desafio
                  </span>
                  <p className="text-slate text-xs leading-relaxed">{proj.challenge}</p>
                </div>
                <div>
                  <span className="text-teal font-mono text-xs uppercase tracking-wider block mb-1">
                    💻 A Solução
                  </span>
                  <p className="text-slate text-xs leading-relaxed">{proj.solution}</p>
                </div>
                <div>
                  <span className="text-teal font-mono text-xs uppercase tracking-wider block mb-1">
                    📈 O Resultado
                  </span>
                  <p className="text-lightest-slate text-xs leading-relaxed font-medium">
                    {proj.result}
                  </p>
                </div>
              </div>

              {/* Technologies Badges */}
              <div className="flex flex-wrap gap-2 mt-4">
                {proj.tags.map((tag, j) => (
                  <span
                    key={j}
                    className="px-3 py-1 text-xs font-mono text-teal bg-teal-tint rounded-full"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

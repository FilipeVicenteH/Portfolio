import { useState } from 'react';
import { motion } from 'framer-motion';

const jobs = [
  {
    company: 'Unico Drop',
    title: 'TI — Suporte Técnico',
    period: 'Junho 2024 — Presente',
    tasks: [
      'Realizo atendimento técnico (N1/N2), solucionando incidentes e reduzindo tempo de resposta ao cliente.',
      'Atuo na resolução de problemas envolvendo integrações via API e Webhooks entre plataformas.',
      'Configuro e dou suporte a automações de mensagens (WhatsApp, e-mail e fluxos automatizados).',
      'Implemento e corrijo plugins de rastreamento e integrações com lojas (Shopify, NuvemShop, etc).',
      'Conduzo onboarding de novos clientes, garantindo ativação e uso correto da plataforma.',
      'Atuo em Customer Success, auxiliando clientes na melhor utilização da ferramenta.',
      'Desenvolvo melhorias Front-End (HTML, CSS, JS, React) com foco em UX/UI.',
      'Crio dashboards em Power BI para análise de dados e apoio estratégico.',
    ],
  },
  {
    company: 'Levlife',
    title: 'Design — Social Mídia',
    period: 'Março 2022 — Agosto 2023',
    tasks: [
      'Criei conteúdos e artes digitais, aumentando o engajamento da marca.',
      'Gerenciei e-commerce e plataformas digitais.',
      'Planejei campanhas digitais e organização de conteúdo.',
    ],
  },
  {
    company: '2º Tabelião de Protestos',
    title: 'Auxiliar de Cartório',
    period: 'Maio 2021 — Fevereiro 2022',
    tasks: [
      'Análise e organização de documentos com alto volume de demanda.',
      'Atendimento ao cliente e suporte administrativo.',
      'Otimização de processos internos, garantindo maior eficiência operacional.',
    ],
  },
];

export default function Experience() {
  const [activeTab, setActiveTab] = useState(0);

  return (
    <section id="experience" className="py-24 px-6 md:px-12 max-w-4xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-100px' }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="section-heading">
          <span className="num">02.</span> Histórico Profissional
        </h2>

        <div className="flex flex-col md:flex-row gap-0">
          {/* Tab List */}
          <div className="flex md:flex-col overflow-x-auto md:overflow-visible border-b md:border-b-0 md:border-l border-navy-lighter shrink-0">
            {jobs.map((job, i) => (
              <button
                key={i}
                onClick={() => setActiveTab(i)}
                className={`px-5 py-3 text-sm font-mono text-left whitespace-nowrap transition-all duration-200 border-b-2 md:border-b-0 md:border-l-2 -mb-px md:mb-0 md:-ml-px ${
                  activeTab === i
                    ? 'text-teal border-teal bg-navy-light/50'
                    : 'text-slate border-transparent hover:text-teal hover:bg-navy-light/30'
                }`}
              >
                {job.company}
              </button>
            ))}
          </div>

          {/* Tab Panel */}
          <div className="pt-5 md:pt-1 md:pl-8 min-h-[320px]">
            <motion.div
              key={activeTab}
              initial={{ opacity: 0, x: 10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.25 }}
            >
              <h3 className="text-lightest-slate text-xl font-semibold">
                {jobs[activeTab].title}{' '}
                <span className="text-teal">@ {jobs[activeTab].company}</span>
              </h3>
              <p className="font-mono text-sm text-slate mt-1 mb-6">
                {jobs[activeTab].period}
              </p>
              <ul className="space-y-3">
                {jobs[activeTab].tasks.map((task, i) => (
                  <li key={i} className="flex items-start gap-3 text-sm leading-relaxed">
                    <span className="text-teal font-mono text-xs mt-1.5 shrink-0">▹</span>
                    <span>{task}</span>
                  </li>
                ))}
              </ul>
            </motion.div>
          </div>
        </div>
      </motion.div>
    </section>
  );
}

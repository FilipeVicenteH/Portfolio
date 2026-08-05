import { useState } from 'react';
import { motion } from 'framer-motion';

const jobs = [
  {
    company: 'Unico Drop',
    title: 'TI — Suporte Técnico',
    period: 'Jun 2024 — Presente',
    tasks: [
      'Atendo chamados técnicos N1/N2, diagnosticando e resolvendo incidentes que impactam a operação dos clientes.',
      'Investigo e corrijo falhas em integrações de API e Webhooks entre a plataforma e sistemas externos.',
      'Configuro automações de disparo de mensagens via WhatsApp e e-mail, criando e ajustando fluxos automatizados.',
      'Implemento e faço manutenção de plugins de rastreamento e integrações com Shopify, NuvemShop e outras plataformas de e-commerce.',
      'Faço o onboarding de clientes novos, garantindo que ativem e usem a plataforma corretamente desde o primeiro dia.',
      'Acompanho clientes ativos com foco em Customer Success, ajudando a extrair mais valor da ferramenta.',
      'Codifico melhorias no front-end (HTML, CSS, JavaScript, React) priorizando usabilidade e experiência do usuário.',
      'Monto dashboards em Power BI para apoiar decisões do time com análise de dados.',
    ],
  },
  {
    company: 'Levlife',
    title: 'Design — Social Media',
    period: 'Mar 2022 — Ago 2023',
    tasks: [
      'Produzi peças gráficas e conteúdos digitais que aumentaram o engajamento nas redes da marca.',
      'Gerenciei o e-commerce da empresa e administrei plataformas digitais de venda.',
      'Planejei e organizei campanhas digitais, definindo calendário editorial e estratégia de conteúdo.',
    ],
  },
  {
    company: '2º Tabelião de Protestos e Notas — SCS',
    title: 'Auxiliar de Cartório',
    period: 'Mai 2021 — Fev 2022',
    tasks: [
      'Analisei e organizei documentos jurídicos com alto volume diário de demanda.',
      'Realizei atendimento presencial ao público, tirando dúvidas e direcionando solicitações.',
      'Identifiquei e implementei melhorias nos processos internos, reduzindo retrabalho.',
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
          <span className="num">02.</span> Onde já trabalhei
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

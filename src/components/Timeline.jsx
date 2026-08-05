import { motion } from 'framer-motion';
import { Briefcase, GraduationCap, Award } from 'lucide-react';

export default function Timeline() {
  const experiences = [
    {
      title: "TI - Suporte Técnico",
      company: "Unico Drop",
      period: "06/2024 - Atual",
      description: [
        "Atendimento técnico (N1/N2), solucionando incidentes e reduzindo tempo de resposta ao cliente.",
        "Resolução de problemas envolvendo integrações via API e Webhooks entre plataformas.",
        "Suporte a automações de mensagens e configuração de plugins de rastreamento (Shopify, NuvemShop, etc).",
        "Onboarding de clientes e Customer Success.",
        "Melhorias Front-End (HTML, CSS, JS, React) com foco em UX/UI e dashboards em Power BI."
      ]
    },
    {
      title: "Design - Social Mídia",
      company: "Levlife",
      period: "03/2022 - 08/2023",
      description: [
        "Criação de conteúdos e artes digitais, aumentando o engajamento da marca.",
        "Gerenciamento de e-commerce e plataformas digitais.",
        "Planejamento de campanhas digitais e organização de conteúdo."
      ]
    },
    {
      title: "Auxiliar de Cartório",
      company: "Segundo Tabelião de Protestos e Notas (SCS)",
      period: "05/2021 - 02/2022",
      description: [
        "Análise e organização de documentos com alto volume de demanda.",
        "Atendimento ao cliente e suporte administrativo.",
        "Otimização de processos internos."
      ]
    }
  ];

  const education = [
    {
      course: "Bacharelado em Ciências da Computação",
      institution: "Centro Universitário União das Américas Descomplica",
      period: "Conclusão: Julho/2026",
      icon: <GraduationCap size={24} className="text-primary" />
    },
    {
      course: "Tecnólogo em Design Gráfico",
      institution: "Faculdade Uninove",
      period: "Conclusão: Julho/2020",
      icon: <GraduationCap size={24} className="text-accent" />
    }
  ];

  const certs = [
    "Web Design (Jorge Street - 2014)",
    "Inglês Intermediário (Count Down - 2016)",
    "Modelagem 3D (All Net - 2014)",
    "Excel Intermediário (Uninove - 2019)"
  ];

  return (
    <section className="py-20 px-6 max-w-4xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        className="mb-16"
      >
        <div className="flex items-center gap-4 mb-8">
          <Briefcase className="text-primary" size={32} />
          <h3 className="text-3xl font-bold text-white">Histórico Profissional</h3>
        </div>

        <div className="space-y-12 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-white/10 before:to-transparent">
          {experiences.map((exp, index) => (
            <div key={index} className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
              <div className="flex items-center justify-center w-10 h-10 rounded-full border border-white/10 bg-surfaceHighlight shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow-xl">
                <div className="w-2 h-2 rounded-full bg-primary/80 group-hover:bg-primary transition-colors"></div>
              </div>
              <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-surface p-6 rounded-2xl border border-white/5 group-hover:border-primary/30 transition-colors hover:-translate-y-1 duration-300">
                <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-2">
                  <h4 className="text-lg font-bold text-white">{exp.title}</h4>
                  <span className="text-sm font-medium text-primary px-3 py-1 bg-primary/10 rounded-full whitespace-nowrap mt-2 sm:mt-0">{exp.period}</span>
                </div>
                <h5 className="text-accent text-sm font-semibold mb-4">{exp.company}</h5>
                <ul className="space-y-2 text-sm text-gray-400">
                  {exp.description.map((item, i) => (
                    <li key={i} className="flex items-start gap-2">
                      <span className="text-primary mt-1">•</span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          ))}
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        className="grid grid-cols-1 md:grid-cols-2 gap-8"
      >
        <div>
          <h3 className="text-2xl font-bold text-white mb-6 flex items-center gap-3"><GraduationCap className="text-primary"/> Formação</h3>
          <div className="space-y-4">
            {education.map((edu, i) => (
              <div key={i} className="bg-surface p-6 rounded-2xl border border-white/5 hover:border-white/10 transition-colors hover:-translate-y-1 duration-300">
                <div className="mb-2">{edu.icon}</div>
                <h4 className="font-bold text-white mb-1">{edu.course}</h4>
                <p className="text-sm text-gray-400 mb-2">{edu.institution}</p>
                <p className="text-xs text-primary bg-primary/10 inline-block px-2 py-1 rounded-md">{edu.period}</p>
              </div>
            ))}
          </div>
        </div>

        <div>
          <h3 className="text-2xl font-bold text-white mb-6 flex items-center gap-3"><Award className="text-accent"/> Certificações</h3>
          <div className="bg-surface p-6 rounded-2xl border border-white/5 hover:border-white/10 transition-colors h-full flex flex-col justify-center hover:-translate-y-1 duration-300">
            <ul className="space-y-4">
              {certs.map((cert, i) => (
                <li key={i} className="flex items-center gap-3 text-gray-300">
                  <div className="w-1.5 h-1.5 rounded-full bg-accent"></div>
                  {cert}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </motion.div>
    </section>
  );
}

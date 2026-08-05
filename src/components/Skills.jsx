import { motion } from 'framer-motion';

const skillCategories = [
  {
    title: 'Front-End',
    skills: ['HTML', 'CSS', 'JavaScript', 'React', 'Tailwind CSS', 'Bootstrap'],
  },
  {
    title: 'Back-End & APIs',
    skills: ['Node.js', 'APIs REST', 'Webhooks'],
  },
  {
    title: 'Banco de Dados',
    skills: ['SQL', 'PostgreSQL', 'Oracle'],
  },
  {
    title: 'Suporte & Infraestrutura',
    skills: ['Troubleshooting N1/N2', 'Help Desk', 'Suporte Remoto', 'Sistemas de Chamados'],
  },
  {
    title: 'Integrações & E-commerce',
    skills: ['API REST', 'Webhooks', 'Shopify', 'NuvemShop'],
  },
  {
    title: 'Sistemas & Redes',
    skills: ['Windows', 'Linux', 'iOS', 'TCP/IP', 'DNS', 'DHCP'],
  },
  {
    title: 'Hardware',
    skills: ['Montagem de PCs', 'Manutenção', 'Instalação de Software'],
  },
  {
    title: 'Design & Ferramentas',
    skills: ['Figma', 'Photoshop', 'Illustrator', 'Git', 'GitHub'],
  },
  {
    title: 'Dados & BI',
    skills: ['Power BI', 'Excel Intermediário'],
  },
];

const softSkills = [
  'Comunicação clara',
  'Pensamento analítico',
  'Organização',
  'Resolução de problemas',
  'Trabalho em equipe',
  'Autodidata',
];

export default function Skills() {
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: { staggerChildren: 0.06 },
    },
  };

  const item = {
    hidden: { opacity: 0, y: 15 },
    show: { opacity: 1, y: 0 },
  };

  return (
    <section id="skills" className="py-24 px-6 md:px-12 max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-100px' }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="section-heading">
          <span className="num">03.</span> Habilidades
        </h2>

        <motion.div
          variants={container}
          initial="hidden"
          whileInView="show"
          viewport={{ once: true, margin: '-50px' }}
          className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          {skillCategories.map((cat, i) => (
            <motion.div
              key={i}
              variants={item}
              className="bg-navy-light p-5 rounded-lg border border-navy-lighter/30 hover:border-teal/20 transition-colors duration-300"
            >
              <h3 className="text-lightest-slate font-semibold text-sm mb-3 flex items-center gap-2">
                <span className="text-teal font-mono text-xs">▹</span>
                {cat.title}
              </h3>
              <div className="flex flex-wrap gap-2">
                {cat.skills.map((skill, j) => (
                  <span
                    key={j}
                    className="px-3 py-1 text-xs font-mono text-teal bg-teal-tint rounded-full"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </motion.div>
          ))}
        </motion.div>

        {/* Competências */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 0.2 }}
          className="mt-12"
        >
          <h3 className="text-lightest-slate font-semibold text-lg mb-4">Competências</h3>
          <div className="flex flex-wrap gap-3">
            {softSkills.map((skill, i) => (
              <span
                key={i}
                className="px-4 py-2 text-sm text-slate-light border border-navy-lighter rounded-full hover:border-teal/30 hover:text-teal transition-colors duration-200"
              >
                {skill}
              </span>
            ))}
          </div>
        </motion.div>
      </motion.div>
    </section>
  );
}

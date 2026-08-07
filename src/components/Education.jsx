import { motion } from 'framer-motion';

const degrees = [
  {
    course: 'Bacharelado em Ciências da Computação',
    institution: 'Centro Universitário União das Américas Descomplica',
    period: 'Concluído em Julho/2026',
  },
  {
    course: 'Tecnólogo em Design Gráfico',
    institution: 'Faculdade Uninove',
    period: 'Concluído em Julho/2020',
  },
];

const certs = [
  { name: 'Web Design', institution: 'Jorge Street', year: '2014' },
  { name: 'Inglês Intermediário', institution: 'Count Down', year: '2016' },
  { name: 'Modelagem 3D', institution: 'All Net', year: '2014' },
  { name: 'Excel Intermediário', institution: 'Uninove', year: '2019' },
];

export default function Education() {
  return (
    <section id="education" className="py-24 px-6 md:px-12 max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-100px' }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="section-heading">
          <span className="num">05.</span> Formação
        </h2>

        <div className="grid md:grid-cols-2 gap-8 mb-16">
          {degrees.map((deg, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.4, delay: i * 0.15 }}
            >
              <div className="bg-navy-light p-6 rounded-lg border border-navy-lighter/30 hover:border-teal/20 transition-all duration-300">
                <div className="flex items-center gap-3 mb-4">
                  <svg className="text-teal shrink-0" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                    <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
                    <path d="M6 12v5c0 1.657 2.686 3 6 3s6-1.343 6-3v-5" />
                  </svg>
                  <div>
                    <h3 className="text-lightest-slate font-semibold leading-tight">{deg.course}</h3>
                    <p className="text-slate text-sm mt-1">{deg.institution}</p>
                  </div>
                </div>
                <p className="font-mono text-teal text-xs">{deg.period}</p>
              </div>
            </motion.div>
          ))}
        </div>

        <h3 className="text-lightest-slate font-semibold text-lg mb-6 flex items-center gap-3">
          <svg className="text-teal" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <circle cx="12" cy="8" r="6" />
            <path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11" />
          </svg>
          Cursos e Certificados
        </h3>
        <div className="grid sm:grid-cols-2 gap-4">
          {certs.map((cert, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.3, delay: i * 0.1 }}
              className="flex items-start gap-3 p-4 rounded-lg hover:bg-navy-light/50 transition-colors"
            >
              <span className="text-teal font-mono text-xs mt-1">▹</span>
              <div>
                <p className="text-lightest-slate text-sm font-medium">{cert.name}</p>
                <p className="text-slate text-xs">
                  {cert.institution} · <span className="font-mono">{cert.year}</span>
                </p>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

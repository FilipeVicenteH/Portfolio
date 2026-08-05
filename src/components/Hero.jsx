import { motion } from 'framer-motion';

export default function Hero() {
  return (
    <section className="min-h-screen flex flex-col justify-center px-6 md:px-12 max-w-5xl mx-auto pt-24">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4, delay: 0.2 }}
      >
        <p className="font-mono text-teal text-sm md:text-base mb-5">
          Olá, meu nome é
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4, delay: 0.35 }}
      >
        <h1 className="text-4xl sm:text-5xl md:text-7xl font-bold text-white leading-tight">
          Filipe Vicente Hidalgo.
        </h1>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4, delay: 0.5 }}
      >
        <h2 className="text-3xl sm:text-4xl md:text-6xl font-bold text-slate mt-2 leading-tight">
          Construo interfaces e resolvo problemas.
        </h2>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4, delay: 0.65 }}
      >
        <p className="text-slate max-w-xl mt-6 text-base md:text-lg leading-relaxed">
          Trabalho com{' '}
          <span className="text-lightest-slate">desenvolvimento Front-End</span>,{' '}
          <span className="text-lightest-slate">suporte técnico N1/N2</span> e{' '}
          <span className="text-lightest-slate">integrações de sistemas</span>.{' '}
          Tenho formação em Ciência da Computação e Design Gráfico,
          e atualmente estou na{' '}
          <a href="#experience" className="text-teal hover:underline">Unico Drop</a>.
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4, delay: 0.8 }}
        className="mt-10"
      >
        <a
          href="#contact"
          className="inline-block px-7 py-4 border border-teal text-teal font-mono text-sm rounded hover:bg-teal-tint transition-colors duration-200"
        >
          Fale comigo
        </a>
      </motion.div>
    </section>
  );
}

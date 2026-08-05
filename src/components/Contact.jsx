import { motion } from 'framer-motion';

export default function Contact() {
  return (
    <section id="contact" className="py-24 px-6 md:px-12 max-w-3xl mx-auto text-center">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-100px' }}
        transition={{ duration: 0.5 }}
      >
        <p className="font-mono text-teal text-sm mb-3">05. E agora?</p>
        <h2 className="text-4xl md:text-5xl font-bold text-lightest-slate mb-5">
          Vamos conversar
        </h2>
        <p className="text-slate max-w-lg mx-auto mb-10 leading-relaxed">
          Estou buscando oportunidades como Dev Front-End/Back-End Júnior,
          QA ou Suporte Técnico. Se tiver uma vaga, um projeto ou só quiser
          trocar uma ideia sobre tecnologia, pode me chamar.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <a
            href="mailto:filipe_vicente@hotmail.com"
            className="inline-block px-8 py-4 border border-teal text-teal font-mono text-sm rounded hover:bg-teal-tint transition-colors duration-200"
          >
            Enviar e-mail
          </a>
          <a
            href="https://wa.me/5511966152956"
            target="_blank"
            rel="noreferrer"
            className="inline-block px-8 py-4 border border-teal text-teal font-mono text-sm rounded hover:bg-teal-tint transition-colors duration-200"
          >
            Chamar no WhatsApp
          </a>
        </div>
      </motion.div>
    </section>
  );
}

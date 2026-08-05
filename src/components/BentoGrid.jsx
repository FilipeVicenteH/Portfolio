import { motion } from 'framer-motion';
import { Database, Layout, Wrench, MapPin, BarChart } from 'lucide-react';

export default function BentoGrid() {
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: { staggerChildren: 0.1 }
    }
  };

  const item = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0 }
  };

  return (
    <section className="py-20 px-6 max-w-6xl mx-auto">
      <motion.div 
        variants={container}
        initial="hidden"
        whileInView="show"
        viewport={{ once: true }}
        className="grid grid-cols-1 md:grid-cols-4 gap-4"
      >
        {/* Resumo */}
        <motion.div variants={item} className="col-span-1 md:col-span-3 bg-surface p-8 rounded-3xl border border-white/5 relative overflow-hidden group hover:border-primary/50 transition-colors">
          <div className="absolute top-0 right-0 w-32 h-32 bg-primary/10 rounded-full blur-3xl group-hover:bg-primary/20 transition-all"></div>
          <h3 className="text-2xl font-bold mb-4 text-white">Sobre mim</h3>
          <p className="text-gray-400 leading-relaxed">
            Sou formado em Ciência da Computação e Design Gráfico, atuando com Suporte Técnico (N1/N2), integrações de sistemas e desenvolvimento Front-End. Experiência com troubleshooting técnico, APIs, Webhooks, automações e atendimento ao cliente, além de desenvolvimento de interfaces web com foco em usabilidade (UI/UX). Meu perfil analítico, organizado e autodidata facilita resolver problemas complexos.
          </p>
        </motion.div>

        {/* Localização */}
        <motion.div variants={item} className="col-span-1 bg-surface p-8 rounded-3xl border border-white/5 flex flex-col justify-center items-center text-center group hover:border-accent/50 transition-colors">
           <MapPin size={40} className="text-accent mb-4 group-hover:scale-110 transition-transform" />
           <p className="text-sm text-gray-400">Baseado em</p>
           <p className="font-bold text-white">São Caetano do Sul, SP</p>
        </motion.div>

        {/* Front-End */}
        <motion.div variants={item} className="col-span-1 md:col-span-2 bg-surface p-8 rounded-3xl border border-white/5 group hover:border-primary/50 transition-colors relative overflow-hidden">
          <div className="absolute -bottom-10 -right-10 w-40 h-40 bg-primary/5 rounded-full blur-2xl group-hover:bg-primary/10 transition-all"></div>
          <Layout className="text-primary mb-4" size={32} />
          <h4 className="text-lg font-bold text-white mb-2">Front-End & Design</h4>
          <p className="text-gray-400 text-sm">HTML, CSS, JavaScript, React, Tailwind, Bootstrap, Figma, Photoshop, Illustrator</p>
        </motion.div>

        {/* Back-End & DB */}
        <motion.div variants={item} className="col-span-1 bg-surface p-8 rounded-3xl border border-white/5 group hover:border-accent/50 transition-colors">
          <Database className="text-accent mb-4" size={32} />
          <h4 className="text-lg font-bold text-white mb-2">Back-End & DB</h4>
          <p className="text-gray-400 text-sm">Node.js, APIs REST, WebHooks, SQL, PostgreSQL, Oracle</p>
        </motion.div>

        {/* Suporte & Infra */}
        <motion.div variants={item} className="col-span-1 bg-surface p-8 rounded-3xl border border-white/5 group hover:border-primary/50 transition-colors">
          <Wrench className="text-primary mb-4" size={32} />
          <h4 className="text-lg font-bold text-white mb-2">Suporte & Infra</h4>
          <p className="text-gray-400 text-sm">Troubleshooting N1/N2, Redes TCP/IP, SOs (Win, Linux, IOS)</p>
        </motion.div>
        
        {/* Dados */}
        <motion.div variants={item} className="col-span-1 md:col-span-4 bg-surface p-8 rounded-3xl border border-white/5 flex items-center justify-between group hover:border-accent/50 transition-colors">
          <div>
            <h4 className="text-lg font-bold text-white mb-1 flex items-center gap-2"><BarChart className="text-accent" size={20}/> Dados & BI</h4>
            <p className="text-gray-400 text-sm">Criação de dashboards e análise de dados em Power BI e Excel Avançado.</p>
          </div>
        </motion.div>
      </motion.div>
    </section>
  );
}

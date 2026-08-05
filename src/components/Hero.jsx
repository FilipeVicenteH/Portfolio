import { motion } from 'framer-motion';
import { Link, Mail, Phone, ExternalLink, Briefcase } from 'lucide-react';

export default function Hero() {
  return (
    <section className="relative min-h-[80vh] flex flex-col justify-center items-center text-center p-6 overflow-hidden">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-primary/20 via-background to-background -z-10 blur-3xl opacity-50"></div>
      
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="max-w-4xl"
      >
        <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-4 text-white">
          Filipe Vicente <span className="text-primary">Hidalgo</span>
        </h1>
        <h2 className="text-xl md:text-2xl text-gray-400 mb-8 font-light">
          Desenvolvedor <span className="text-white font-medium">Front-End / Back-End Júnior</span> | QA & Suporte Técnico
        </h2>
        
        <div className="flex flex-wrap justify-center gap-4 mb-12">
          <a href="https://github.com/FilipeVicenteH" target="_blank" rel="noreferrer" className="flex items-center gap-2 px-6 py-3 bg-surfaceHighlight hover:bg-white/10 border border-white/5 rounded-full transition-all text-sm font-medium hover:-translate-y-1">
            <Link size={18} /> GitHub
          </a>
          <a href="https://www.linkedin.com/in/filipevicentehidalgo" target="_blank" rel="noreferrer" className="flex items-center gap-2 px-6 py-3 bg-surfaceHighlight hover:bg-white/10 border border-white/5 rounded-full transition-all text-sm font-medium hover:-translate-y-1">
            <Briefcase size={18} /> LinkedIn
          </a>
          <a href="https://www.behance.net/filipevicenteh" target="_blank" rel="noreferrer" className="flex items-center gap-2 px-6 py-3 bg-surfaceHighlight hover:bg-white/10 border border-white/5 rounded-full transition-all text-sm font-medium hover:-translate-y-1">
            <ExternalLink size={18} /> Behance
          </a>
          <a href="mailto:filipe_vicente@hotmail.com" className="flex items-center gap-2 px-6 py-3 bg-surfaceHighlight hover:bg-white/10 border border-white/5 rounded-full transition-all text-sm font-medium hover:-translate-y-1">
            <Mail size={18} /> Email
          </a>
        </div>
      </motion.div>
    </section>
  );
}

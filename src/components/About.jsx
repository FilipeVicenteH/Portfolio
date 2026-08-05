import { motion } from 'framer-motion';

export default function About() {
  return (
    <section id="about" className="py-24 px-6 md:px-12 max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-100px' }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="section-heading">
          <span className="num">01.</span> Sobre mim
        </h2>

        <div className="grid md:grid-cols-3 gap-12">
          <div className="md:col-span-2 space-y-4">
            <p>
              Sou formado em <span className="text-lightest-slate">Ciência da Computação</span> pelo
              Centro Universitário União das Américas Descomplica e em{' '}
              <span className="text-lightest-slate">Design Gráfico</span> pela Faculdade Uninove,
              atuando com Suporte Técnico (N1/N2), integrações de sistemas e desenvolvimento Front-End.
            </p>
            <p>
              Tenho experiência com{' '}
              <span className="text-lightest-slate">troubleshooting técnico</span>, APIs, Webhooks,
              automações e atendimento ao cliente, além de desenvolvimento de interfaces web com foco
              em usabilidade (<span className="text-teal">UI/UX</span>).
            </p>
            <p>
              Atuação com análise de dados em{' '}
              <span className="text-lightest-slate">Power BI</span> e Excel, onboarding de clientes
              e Customer Success. Meu perfil{' '}
              <span className="text-lightest-slate">analítico, organizado e autodidata</span>, com
              facilidade para resolver problemas complexos e aprender novas tecnologias.
            </p>
            <p className="text-lightest-slate font-medium mt-6">
              Objetivo: Atuar como Desenvolvedor Front-End ou Back-End Júnior, QA Teste, Analista de Suporte Técnico.
            </p>
          </div>

          {/* Contact Info Card */}
          <div className="relative">
            <div className="bg-navy-light rounded-lg p-6 border border-navy-lighter/50">
              <h3 className="text-lightest-slate font-semibold text-lg mb-4">Informações</h3>
              <ul className="space-y-3 text-sm">
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Localização</span>
                    <span className="text-lightest-slate">Barcelona — São Caetano do Sul, SP</span>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Email</span>
                    <a href="mailto:filipe_vicente@hotmail.com" className="text-lightest-slate hover:text-teal transition-colors">
                      filipe_vicente@hotmail.com
                    </a>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Telefone / WhatsApp</span>
                    <span className="text-lightest-slate">(11) 96615-2956</span>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">LinkedIn</span>
                    <a href="https://www.linkedin.com/in/filipevicentehidalgo" target="_blank" rel="noreferrer" className="text-lightest-slate hover:text-teal transition-colors break-all">
                      linkedin.com/in/filipevicentehidalgo
                    </a>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">Behance</span>
                    <a href="https://www.behance.net/filipevicenteh" target="_blank" rel="noreferrer" className="text-lightest-slate hover:text-teal transition-colors">
                      behance.net/filipevicenteh
                    </a>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-teal font-mono text-xs mt-0.5">▹</span>
                  <div>
                    <span className="text-slate-light block text-xs uppercase tracking-wider mb-0.5">GitHub</span>
                    <a href="https://github.com/FilipeVicenteH" target="_blank" rel="noreferrer" className="text-lightest-slate hover:text-teal transition-colors">
                      github.com/FilipeVicenteH
                    </a>
                  </div>
                </li>
              </ul>
            </div>
            {/* Decorative offset border */}
            <div className="absolute -z-10 top-3 left-3 w-full h-full border border-teal/30 rounded-lg"></div>
          </div>
        </div>
      </motion.div>
    </section>
  );
}

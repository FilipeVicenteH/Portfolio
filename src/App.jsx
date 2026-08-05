import Hero from './components/Hero';
import BentoGrid from './components/BentoGrid';
import Timeline from './components/Timeline';

function App() {
  return (
    <div className="min-h-screen selection:bg-primary/30">
      <main>
        <Hero />
        <BentoGrid />
        <Timeline />
      </main>
      
      <footer className="py-8 text-center text-sm text-gray-500 border-t border-white/5 mt-10">
        <p>© {new Date().getFullYear()} Filipe Vicente Hidalgo. Todos os direitos reservados.</p>
        <p className="mt-2 text-xs">Desenvolvido com React, TailwindCSS & Framer Motion</p>
      </footer>
    </div>
  );
}

export default App;

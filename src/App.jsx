import Navbar from './components/Navbar';
import SideElements from './components/SideElements';
import Hero from './components/Hero';
import About from './components/About';
import Experience from './components/Experience';
import Skills from './components/Skills';
import Education from './components/Education';
import Contact from './components/Contact';

function App() {
  return (
    <div className="min-h-screen">
      <Navbar />
      <SideElements />

      <main className="md:pl-12 md:pr-12">
        <Hero />
        <About />
        <Experience />
        <Skills />
        <Education />
        <Contact />
      </main>

      <footer className="py-6 text-center font-mono text-xs text-slate">
        <a
          href="https://github.com/FilipeVicenteH"
          target="_blank"
          rel="noreferrer"
          className="hover:text-teal transition-colors"
        >
          Desenvolvido por Filipe Vicente Hidalgo
        </a>
      </footer>
    </div>
  );
}

export default App;

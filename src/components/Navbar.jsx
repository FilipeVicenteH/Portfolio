import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const navLinks = [
  { num: '01', label: 'Sobre', href: '#about' },
  { num: '02', label: 'Experiência', href: '#experience' },
  { num: '03', label: 'Projetos', href: '#projects' },
  { num: '04', label: 'Habilidades', href: '#skills' },
  { num: '05', label: 'Formação', href: '#education' },
  { num: '06', label: 'Contato', href: '#contact' },
];

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [hidden, setHidden] = useState(false);
  const [lastScrollY, setLastScrollY] = useState(0);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;
      setScrolled(currentScrollY > 50);
      setHidden(currentScrollY > lastScrollY && currentScrollY > 100);
      setLastScrollY(currentScrollY);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, [lastScrollY]);

  return (
    <>
      <motion.header
        initial={{ y: -100 }}
        animate={{ y: hidden && !menuOpen ? -100 : 0 }}
        transition={{ duration: 0.3 }}
        className={`fixed top-0 left-0 right-0 z-50 px-6 md:px-12 py-4 transition-all duration-300 ${
          scrolled ? 'bg-navy/90 backdrop-blur-md shadow-lg shadow-navy/50' : ''
        }`}
      >
        <nav className="max-w-5xl mx-auto flex items-center justify-between">
          <a href="#" className="text-teal font-mono font-medium text-lg hover:opacity-80 transition-opacity">
            {'<FVH />'}
          </a>

          {/* Desktop Nav */}
          <ul className="hidden md:flex items-center gap-8">
            {navLinks.map((link) => (
              <li key={link.num}>
                <a
                  href={link.href}
                  className="text-sm text-lightest-slate hover:text-teal transition-colors font-mono"
                >
                  <span className="text-teal">{link.num}.</span> {link.label}
                </a>
              </li>
            ))}
          </ul>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setMenuOpen(!menuOpen)}
            className="md:hidden relative z-50 w-8 h-8 flex flex-col justify-center items-center gap-1.5"
            aria-label="Menu"
          >
            <span className={`block w-6 h-0.5 bg-teal transition-all duration-300 ${menuOpen ? 'rotate-45 translate-y-2' : ''}`} />
            <span className={`block w-6 h-0.5 bg-teal transition-all duration-300 ${menuOpen ? 'opacity-0' : ''}`} />
            <span className={`block w-6 h-0.5 bg-teal transition-all duration-300 ${menuOpen ? '-rotate-45 -translate-y-2' : ''}`} />
          </button>
        </nav>
      </motion.header>

      {/* Mobile Menu */}
      <AnimatePresence>
        {menuOpen && (
          <motion.div
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'tween', duration: 0.3 }}
            className="fixed inset-0 z-40 bg-navy-light/95 backdrop-blur-md flex items-center justify-center md:hidden"
          >
            <ul className="flex flex-col items-center gap-8">
              {navLinks.map((link) => (
                <li key={link.num}>
                  <a
                    href={link.href}
                    onClick={() => setMenuOpen(false)}
                    className="text-lg text-lightest-slate hover:text-teal transition-colors font-mono"
                  >
                    <span className="text-teal block text-center text-sm mb-1">{link.num}.</span>
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}

// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><a href="00-preface.html"><strong aria-hidden="true">0.</strong> Preface</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="00-preface/01-motivation.html"><strong aria-hidden="true">0.1.</strong> Motivation</a></li><li class="chapter-item "><a href="00-preface/02-getting_started.html"><strong aria-hidden="true">0.2.</strong> Getting Started</a></li><li class="chapter-item "><a href="00-preface/03-mdbook_usage.html"><strong aria-hidden="true">0.3.</strong> Usage of This Website</a></li></ol></li><li class="chapter-item expanded "><li class="spacer"></li><li class="chapter-item expanded "><a href="01-fundamentals.html"><strong aria-hidden="true">1.</strong> Fundamentals</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="01-fundamentals/01-unsigned_binary_integers.html"><strong aria-hidden="true">1.1.</strong> Unsigned Binary Integers</a></li><li class="chapter-item "><a href="01-fundamentals/02-signed_binary_integers.html"><strong aria-hidden="true">1.2.</strong> Signed Binary Integers</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="01-fundamentals/02-signed_binary_integers/01-sign_and_magnitude.html"><strong aria-hidden="true">1.2.1.</strong> Sign and Magnitude</a></li><li class="chapter-item "><a href="01-fundamentals/02-signed_binary_integers/02-ones_complement.html"><strong aria-hidden="true">1.2.2.</strong> One&#39;s Complement</a></li><li class="chapter-item "><a href="01-fundamentals/02-signed_binary_integers/03-twos_complement.html"><strong aria-hidden="true">1.2.3.</strong> Two&#39;s Complement</a></li></ol></li><li class="chapter-item "><a href="01-fundamentals/03-logic_gates.html"><strong aria-hidden="true">1.3.</strong> Logic Gates</a></li><li class="chapter-item "><a href="01-fundamentals/04-bitwise_operators.html"><strong aria-hidden="true">1.4.</strong> Bitwise Operators</a></li><li class="chapter-item "><a href="01-fundamentals/05-arithmetic_operators.html"><strong aria-hidden="true">1.5.</strong> Arithmetic Operators</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="01-fundamentals/05-arithmetic_operators/01-impl_multiplication.html"><strong aria-hidden="true">1.5.1.</strong> Implementation of Multiplication</a></li><li class="chapter-item "><a href="01-fundamentals/05-arithmetic_operators/02-impl_division.html"><strong aria-hidden="true">1.5.2.</strong> Implementation of Division</a></li><li class="chapter-item "><a href="01-fundamentals/05-arithmetic_operators/03-edge_cases.html"><strong aria-hidden="true">1.5.3.</strong> Handling Edge Cases</a></li></ol></li><li class="chapter-item "><a href="01-fundamentals/06-unit_tests.html"><strong aria-hidden="true">1.6.</strong> Unit Tests</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="01-fundamentals/06-unit_tests/01-example_based_tests.html"><strong aria-hidden="true">1.6.1.</strong> Example Based Tests</a></li><li class="chapter-item "><a href="01-fundamentals/06-unit_tests/02-property_based_tests.html"><strong aria-hidden="true">1.6.2.</strong> Property Based Tests</a></li></ol></li></ol></li><li class="chapter-item expanded "><a href="02-symbolic_computation.html"><strong aria-hidden="true">2.</strong> Symbolic Computation</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="02-symbolic_computation/01-basic_operations.html"><strong aria-hidden="true">2.1.</strong> Basic Operations</a></li><li class="chapter-item "><a href="02-symbolic_computation/02-calculus.html"><strong aria-hidden="true">2.2.</strong> Calculus</a></li><li class="chapter-item "><a href="02-symbolic_computation/03-hydrogen_atom.html"><strong aria-hidden="true">2.3.</strong> Hydrogen Atom</a></li><li class="chapter-item "><a href="02-symbolic_computation/04-harmonic_oscillator.html"><strong aria-hidden="true">2.4.</strong> Harmonic Oscillator</a></li></ol></li><li class="chapter-item expanded "><a href="03-molecular_integrals.html"><strong aria-hidden="true">3.</strong> Molecular Integrals</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><div><strong aria-hidden="true">3.0.</strong> Latest Scripts</div></li><li class="chapter-item "><a href="03-molecular_integrals/01-gaussian_orbitals.html"><strong aria-hidden="true">3.1.</strong> Gaussian Type Orbitals</a></li><li class="chapter-item "><a href="03-molecular_integrals/02-hermite_gaussians.html"><strong aria-hidden="true">3.2.</strong> Hermite Gaussians</a></li><li class="chapter-item "><a href="03-molecular_integrals/03-overlap_integrals.html"><strong aria-hidden="true">3.3.</strong> Overlap Integrals</a></li><li class="chapter-item "><a href="03-molecular_integrals/04-testing_on_molecules.html"><strong aria-hidden="true">3.4.</strong> Testing on Molecules</a></li><li class="chapter-item "><div><strong aria-hidden="true">3.5.</strong> Nuclear Attraction Integrals</div></li><li class="chapter-item "><div><strong aria-hidden="true">3.6.</strong> Electron Repulsion Integrals</div></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">4.</strong> Numerical Optimisation</div><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><div><strong aria-hidden="true">4.1.</strong> Convergence</div></li><li class="chapter-item "><div><strong aria-hidden="true">4.2.</strong> Test Functions</div></li><li class="chapter-item "><div><strong aria-hidden="true">4.3.</strong> Steepest Descent</div></li><li class="chapter-item "><div><strong aria-hidden="true">4.4.</strong> (Quasi-)Newton Methods</div></li><li class="chapter-item "><div><strong aria-hidden="true">4.5.</strong> Desired Properties</div></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">5.</strong> The Hartree Fock Approximation</div><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><div><strong aria-hidden="true">5.1.</strong> The SCF Procedure</div></li><li class="chapter-item "><div><strong aria-hidden="true">5.2.</strong> Plot Grid Data</div></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">6.</strong> Configuration Interaction</div><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><div><strong aria-hidden="true">6.1.</strong> Configuration Interaction Singles</div></li><li class="chapter-item "><div><strong aria-hidden="true">6.2.</strong> Second Quantisation</div><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><div><strong aria-hidden="true">6.2.1.</strong> Introduction</div></li><li class="chapter-item "><div><strong aria-hidden="true">6.2.2.</strong> Matrix Elements</div></li><li class="chapter-item "><div><strong aria-hidden="true">6.2.3.</strong> CIS Revisited</div></li><li class="chapter-item "><div><strong aria-hidden="true">6.2.4.</strong> Representation of Ladder Operators</div></li></ol></li><li class="chapter-item "><div><strong aria-hidden="true">6.3.</strong> Full Configuration Interaction</div></li></ol></li><li class="chapter-item expanded "><li class="spacer"></li><li class="chapter-item expanded affix "><a href="psets/pset_00.html">Problem Set 0</a></li><li class="chapter-item expanded affix "><div>Problem Set 1</div></li><li class="chapter-item expanded affix "><div>Problem Set 2</div></li><li class="chapter-item expanded affix "><div>Problem Set 3</div></li><li class="chapter-item expanded affix "><div>Problem Set 4</div></li><li class="chapter-item expanded affix "><a href="psets/sol_pset_00.html">Solution to Problem Set 0</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);

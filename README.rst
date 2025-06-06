.. image:: https://raw.githubusercontent.com/Ombucha/pirate.py/main/banner.png

.. image:: https://img.shields.io/pypi/v/pirate.py
    :target: https://pypi.python.org/pypi/pirate.py
    :alt: PyPI version
.. image:: https://img.shields.io/pypi/dm/pirate.py
    :target: https://pypi.python.org/pypi/pirate.py
    :alt: PyPI downloads
.. image:: https://sloc.xyz/github/Ombucha/pirate.py
    :target: https://github.com/Ombucha/pirate.py/graphs/contributors
    :alt: Lines of code
.. image:: https://img.shields.io/github/repo-size/Ombucha/pirate.py
    :target: https://github.com/Ombucha/pirate.py
    :alt: Repository size

Arrr! What Ye Be Needin'
------------------------

Before ye set sail, make sure yer ship has these aboard:

* Python 3.8 or higher (no rusty old versions, matey!)
* The mighty `requests <https://pypi.python.org/pypi/requests>`_ library

How t' Hoist the Sails (Installin')
-----------------------------------

To plunder the latest stable release from PyPI, run this in yer terminal:

.. code-block:: sh

    # Fer Unix / macOS buccaneers
    python3 -m pip install "pirate.py"

    # Fer Windows deckhands
    py -m pip install "pirate.py"

If ye want the freshest code from the captain's quarters (development version):

.. code-block:: sh

    git clone https://github.com/Ombucha/pirate.py
    cd pirate.py
    pip install -e .

Quick Start Fer Landlubbers
---------------------------

Here be how ye use this treasure:

.. code-block:: python

    import pirate

    # Hurl a pirate insult at yer foes!
    print(pirate.insult())  # "We'll keel-haul ye, ye fish-kissin', scallywagging monkey! ... Ahoy!"

    # Turn yer plain English into Pirate Speak!
    print(pirate.translate("Hand over the treasure, or you'll be walking the plank!"))  # "Hand o'er the treasure, or ye'll be walkin' the plank!"

Links t' Treasure Maps
----------------------

- `Pirate Monkeyness <https://pirate.monkeyness.com/>`_ — The mystical source o' pirate wisdom!
- `Documentation <https://pirate.readthedocs.io/>`_ — The ship's logs, fer those who read.

Fair winds and happy plunderin', matey! 🏴‍☠️
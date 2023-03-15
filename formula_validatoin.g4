grammar formula_validatoin;


formula: (logic_constant|atomic_formula|complex_formula);


logic_constant: (LOGIC_ZERO|LOGIC_ONE);

atomic_formula: upper_alph;

complex_formula: (unar_complex_formula|bin_complex_formula);

unar_complex_formula: OPEN_CIR_BRACKET NEGATION formula CLOSE_CIR_BRACKET;
bin_complex_formula: OPEN_CIR_BRACKET formula binary_connection formula CLOSE_CIR_BRACKET;

binary_connection: CONJUNCTION|DISJUNCTION|IMPLICATION|EQUIVALENT;
upper_alph: ('A'| 'B'| 'C'| 'D'| 'E'| 'F'| 'G'| 'H'| 'I'| 'J'|'K'| 'L'| 'M'| 'N'| 'O'| 'P'| 'Q'| 'R'| 'S'| 'T'|'U'| 'V'| 'W'| 'X'| 'Y'| 'Z');


NEGATION: '!';
CONJUNCTION: '/\\';
DISJUNCTION: '\\/';
IMPLICATION: '->';
EQUIVALENT: '~';


LOGIC_ONE : '1';
LOGIC_ZERO: '0';

OPEN_CIR_BRACKET: '(';
CLOSE_CIR_BRACKET: ')';
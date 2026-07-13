grammar forth;

program
    : statement* EOF
    ;

statement
    : NUMBER                                            # PushNumber
    | COLON ID body* SEMICOLON                          # DefFunc
    | ID                                                # CallFunc
    ;

body
    : NUMBER                                            # BodyNumber
    | IF thenBlock+=body* (ELSE elseBlock+=body*)? ENDIF  # Conditional
    | ID                                                # BodyCall
    ;

NUMBER      : '-'? [0-9]+ ;

IF          : 'if' ;
ELSE        : 'else' ;
ENDIF       : 'endif' ;
COLON       : ':' ;
SEMICOLON   : ';' ;

ID          : [a-zA-Z0-9_+\-*/<>=.][a-zA-Z0-9_+\-*/<>=.]* ;

COMMENT     : '(' ~[)]* ')' -> skip ;
WS          : [ \t\r\n]+ -> skip ;

LEXICAL_ERROR : . ;

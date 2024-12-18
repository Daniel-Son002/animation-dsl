
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'sexpr_listBOOLEAN DEFINE ID LPAREN NUMBER RPAREN STRINGsexpr_list : sexpr\n| sexpr_list sexprsexpr : LPAREN ID param_list RPAREN\n| define_exprdefine_expr : LPAREN DEFINE ID param_list LPAREN sexpr_list RPAREN RPARENparam_list : param\n| param_list paramparam : LPAREN ID NUMBER RPAREN\n| LPAREN ID STRING RPAREN\n| LPAREN ID BOOLEAN RPAREN'
    
_lr_action_items = {'LPAREN':([0,1,2,4,5,6,9,10,11,13,14,15,19,20,21,22,23,25,],[3,3,-1,-4,-2,8,8,-6,8,-3,-7,19,3,-8,-9,-10,3,-5,]),'$end':([1,2,4,5,13,25,],[0,-1,-4,-2,-3,-5,]),'RPAREN':([2,4,5,9,10,13,14,16,17,18,20,21,22,23,24,25,],[-1,-4,-2,13,-6,-3,-7,20,21,22,-8,-9,-10,24,25,-5,]),'ID':([3,7,8,19,],[6,11,12,12,]),'DEFINE':([3,],[7,]),'NUMBER':([12,],[16,]),'STRING':([12,],[17,]),'BOOLEAN':([12,],[18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sexpr_list':([0,19,],[1,23,]),'sexpr':([0,1,19,23,],[2,5,2,5,]),'define_expr':([0,1,19,23,],[4,4,4,4,]),'param_list':([6,11,],[9,15,]),'param':([6,9,11,15,],[10,14,10,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sexpr_list","S'",1,None,None,None),
  ('sexpr_list -> sexpr','sexpr_list',1,'p_sexpr_list','interpret.py',50),
  ('sexpr_list -> sexpr_list sexpr','sexpr_list',2,'p_sexpr_list','interpret.py',51),
  ('sexpr -> LPAREN ID param_list RPAREN','sexpr',4,'p_sexpr','interpret.py',58),
  ('sexpr -> define_expr','sexpr',1,'p_sexpr','interpret.py',59),
  ('define_expr -> LPAREN DEFINE ID param_list LPAREN sexpr_list RPAREN RPAREN','define_expr',8,'p_define_expr','interpret.py',66),
  ('param_list -> param','param_list',1,'p_param_list','interpret.py',74),
  ('param_list -> param_list param','param_list',2,'p_param_list','interpret.py',75),
  ('param -> LPAREN ID NUMBER RPAREN','param',4,'p_param','interpret.py',82),
  ('param -> LPAREN ID STRING RPAREN','param',4,'p_param','interpret.py',83),
  ('param -> LPAREN ID BOOLEAN RPAREN','param',4,'p_param','interpret.py',84),
]

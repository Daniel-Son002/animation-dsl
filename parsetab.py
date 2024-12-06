
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'sexpr_listDEFINE ID LPAREN NUMBER RPARENsexpr_list : sexpr\n                  | sexpr_list sexprsexpr : LPAREN ID param_list RPAREN\n             | define_exprdefine_expr : LPAREN DEFINE ID param_list LPAREN sexpr_list RPAREN RPARENparam_list : param\n                  | param_list paramparam : LPAREN ID NUMBER RPAREN'
    
_lr_action_items = {'LPAREN':([0,1,2,4,5,6,9,10,11,13,14,15,17,18,19,21,],[3,3,-1,-4,-2,8,8,-6,8,-3,-7,17,3,-8,3,-5,]),'$end':([1,2,4,5,13,21,],[0,-1,-4,-2,-3,-5,]),'RPAREN':([2,4,5,9,10,13,14,16,18,19,20,21,],[-1,-4,-2,13,-6,-3,-7,18,-8,20,21,-5,]),'ID':([3,7,8,17,],[6,11,12,12,]),'DEFINE':([3,],[7,]),'NUMBER':([12,],[16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sexpr_list':([0,17,],[1,19,]),'sexpr':([0,1,17,19,],[2,5,2,5,]),'define_expr':([0,1,17,19,],[4,4,4,4,]),'param_list':([6,11,],[9,15,]),'param':([6,9,11,15,],[10,14,10,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sexpr_list","S'",1,None,None,None),
  ('sexpr_list -> sexpr','sexpr_list',1,'p_sexpr_list','interpret.py',38),
  ('sexpr_list -> sexpr_list sexpr','sexpr_list',2,'p_sexpr_list','interpret.py',39),
  ('sexpr -> LPAREN ID param_list RPAREN','sexpr',4,'p_sexpr','interpret.py',46),
  ('sexpr -> define_expr','sexpr',1,'p_sexpr','interpret.py',47),
  ('define_expr -> LPAREN DEFINE ID param_list LPAREN sexpr_list RPAREN RPAREN','define_expr',8,'p_define_expr','interpret.py',54),
  ('param_list -> param','param_list',1,'p_param_list','interpret.py',62),
  ('param_list -> param_list param','param_list',2,'p_param_list','interpret.py',63),
  ('param -> LPAREN ID NUMBER RPAREN','param',4,'p_param','interpret.py',70),
]

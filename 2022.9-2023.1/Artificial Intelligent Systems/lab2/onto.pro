c("person").

pr(["name"]).
pr(["age", "old"]).
pr(["has_sex"]).
pr(["male"]).
pr(["female"]).

g(down,["has_child","is_grandparent", "is_uncle","is_father","is_mother","is_grandfather", "is_grandmother"]).
g(up, ["is_a", "is_child", "is_son", "is_daughter", "is_grandchild", "is_grandson", "is_nephew"]).
g(side,["is_cousin", "is_sibling", "is_sister", "is_brother", "is_wife", "is_husband", "married"]).

r( [t("?x","has_child","?y"),t("?x","is_a","person")], 
   [t("?y","is_a","person")] ).
r( [t("?x","married","?y"),t("?x","is_a","person")], 
   [t("?y","is_a","person")] ).

r( [ t("?x", "married", "?y"), t("?x", "has_sex", "male") ], 
   [ t("?y", "has_sex", "female") ]). 
r( [ t("?x", "married", "?y"), t("?x", "has_sex", "female") ], 
   [ t("?y", "has_sex", "male") ]). 
   
r( [ t("?x", "married", "?y"), t("?x", "has_child", "?z") ], 
   [ t("?y", "has_child", "?z") ]). 
   
r( [t("?x","married","?y")], [t("?y","married","?x")] ). 

r( [t("?x","married","?y"),t("?x","has_sex","male")], 
   [t("?x","is_husband","?y")] ).
   
r( [t("?x","is_husband","?y")], [t("?y","is_wife","?x")] ). 

r( [t("?x","is_sibling","?y")], [t("?y","is_sibling","?x")] ). 
r( [t("?x","has_child","?y"),t("?x","has_sex","male")], 
   [t("?x","is_father","?y")] ).
r( [t("?x","has_child","?y"),t("?x","has_sex","male")], 
   [t("?x","is_father","?y")] ).
      
r( [t("?x","has_child","?y"),t("?x","has_sex","female")], 
   [t("?x","is_mother","?y")] ).
r( [t("?x","has_child","?y"),t("?x","has_sex","female")], 
   [t("?x","is_mother","?y")] ).

r( [t("?x","has_child","?y")], [t("?y","is_child","?x")] ).
r( [t("?x","is_uncle","?y")], [t("?y","is_nephew","?x")] ).
r( [t("?x","is_aunt","?y")], [t("?y","is_nephew","?x")] ).

r( [t("?x","has_child","?y"),t("?y","has_child","?z")], 
   [t("?x","is_grandparent","?z")] ).
r( [t("?x","is_grandparent","?y"),t("?x","has_sex","male")], 
   [t("?x","is_grandfather","?y")] ).   
r( [t("?x","is_grandparent","?y"),t("?x","has_sex","male")], 
   [t("?x","is_grandfather","?y")] ). 
      
r( [t("?x","is_grandparent","?y"),t("?x","has_sex","female")], 
   [t("?x","is_grandmother","?y")] ).   
r( [t("?x","is_grandparent","?y"),t("?x","has_sex","female")], 
   [t("?x","is_grandmother","?y")] ). 
   
r( [t("?x","has_child","?y"),t("?x","has_child","?z"),t("?y","differs","?z")], 
   [t("?y","is_sibling","?z")] ).
   
r( [t("?x","is_sibling","?y"),t("?x","has_sex","male")], 
   [t("?x","is_brother","?y")] ).   
r( [t("?x","is_sibling","?y"),t("?x","has_sex","male")], 
   [t("?x","is_brother","?y")] ). 
      
r( [t("?x","is_sibling","?y"),t("?x","has_sex","female")], 
   [t("?x","is_sister","?y")] ).    
r( [t("?x","is_sibling","?y"),t("?x","has_sex","female")], 
   [t("?x","is_sister","?y")] ). 
      
r( [t("?x","has_child","?y"),t("?x","is_sibling","?z"),t("?z","has_child","?a"),t("?y", "differs","?a")], 
   [t("?y","is_cousin","?a")] ).

r( [t("?x","has_child","?y"),t("?x","is_sibling","?z"), t("?z","has_sex", "male")], 
   [t("?z","is_uncle", "?y")] ).
r( [t("?x","has_child","?y"),t("?x","is_sibling","?z"), t("?x","has_sex","male")], 
   [t("?z","is_uncle", "?y")] ).
      
r( [t("?x","has_child","?y"),t("?x","is_sibling","?z"), t("?z","has_sex", "female")], 
   [t("?z","is_aunt", "?y")] ).
r( [t("?x","has_child","?y"),t("?x","is_sibling","?z"), t("?x","has_sex","female")], 
   [t("?z","is_aunt", "?y")] ).
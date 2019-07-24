import java.util.Stack;

class ValidParentheses {
    private boolean isValid(String s) {
        if (s.isEmpty()) {
            return true;
        }
        if (s.length() % 2 == 1) {
            return false;
        }
        String[] inArray = s.split("");
        Stack<String> parCheck = new Stack<> ();
        for (int i = 0; i < inArray.length; i++) {
            if ( inArray[i].equals("(") || inArray[i].equals("[") || inArray[i].equals("{")) {
                parCheck.push(inArray[i]);
            } else {
                if (isMatch(inArray[i], parCheck)) {
                    parCheck.pop();
                }
            }
        }
        return parCheck.empty();
    }
    private boolean isMatch(String p, Stack<String> stk) {
        if (stk.empty()) {
            return false;
        } else {
            if (p.equals(")") && stk.peek().equals("(")) {
                return true;
            } else if (p.equals("]") && stk.peek().equals("[")) {
                return true;
            } else if (p.equals("}") && stk.peek().equals("{")) {
                return true;
            } else {
                return false;
            }
        }
    }
    public static void main (String args[]) {
        ValidParentheses vp = new ValidParentheses();
        String test = "";
        System.out.print(vp.isValid(test));
    }
}
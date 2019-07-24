class ArrayStack {
    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int stackPointer = 0;
        for (char c: s.toCharArray()){
            switch (c){
                case '(':
                case '{':
                case '[':
                    stack[stackPointer++] = c;
                    break;
                case ')':
                    if (stackPointer == 0 || stack[--stackPointer] != '(') return false;
                    break;
                case '}':
                    if (stackPointer == 0 || stack[--stackPointer] != '{') return false;
                    break;
                case ']':
                    if (stackPointer == 0 || stack[--stackPointer] != '[') return false;
                    break;
            }
        }
        return stackPointer==0;
    }
}

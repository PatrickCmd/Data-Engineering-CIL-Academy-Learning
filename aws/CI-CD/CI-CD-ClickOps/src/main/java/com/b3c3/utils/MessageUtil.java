package com.b3c3.utils;

public class MessageUtil {
    private String defaultMessage;

    public MessageUtil(){
        this(null);
    }

    public MessageUtil(final String strMsg){
        if ((strMsg != null) && !strMsg.isEmpty()) {
            this.defaultMessage = strMsg.trim();
        }
        else{
            this.defaultMessage = getDefaultMessage();
        }
    }

    private String getDefaultMessage(){
        return new StringBuilder()
            .append("Hi there! Please tell me your name and I'd greet you properly.\n")
            .append("You can run me with MessageUtil <your-name> \n")
            .append("Or you can add many names: MessageUtil <your-name> [<more-names> <more-names>]")
            .toString();
    }

    public String printMessage(){
        return this.printMessage(defaultMessage);
    }

    public String printMessage(final String msg){
        System.out.println(msg);
        return msg;
    }

    public String salutationMessage(final String who){
        String salutationMessage = new StringBuilder()
            .append("Hi! ").append(who)
            .append(".... Nice to meet you!")
            .toString();

        return this.printMessage(salutationMessage);
    }

    public static void main(String[] args) {
        //java -cp target/classes com.b3c3.utils.MessageUtil
        //java -cp target/messageUtil-1.0.jar com.b3c3.utils.MessageUtil

        if (args.length <= 0) {
            new MessageUtil().printMessage();
        }
        else {
            MessageUtil msgUtil = new MessageUtil("");

            for(int i = 0; i < args.length; i++) {
                msgUtil.salutationMessage(args[i]);
            }
        }
    }
}
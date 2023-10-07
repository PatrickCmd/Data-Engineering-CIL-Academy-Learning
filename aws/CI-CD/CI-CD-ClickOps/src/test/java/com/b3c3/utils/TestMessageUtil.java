package com.b3c3.utils;

import org.junit.Test;
//import org.junit.Ignore;
import org.junit.Before;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import static org.hamcrest.CoreMatchers.allOf;
import static org.hamcrest.CoreMatchers.containsString;


public class TestMessageUtil {
    MessageUtil messageUtil = new MessageUtil();

    @Before
    public void BeforeTests(){
        System.out.println("\n-----------------------------------------------");
    }

    @Test
    public void testPrintMessageWithEmptyStringPrintsDefaultMessage() {
        System.out.println("Testing testPrintMessageWithEmptyStringPrintsDefaultMessage....");
        String defaultMsg = "I am the default Message";
        MessageUtil messageUtil = new MessageUtil(defaultMsg);
        assertEquals(defaultMsg, messageUtil.printMessage());
    }

    @Test
    public void testInitialMessageIsTrimmed(){
        String wsMsg = "   White Space to begin and end  ";
        MessageUtil messageUtil = new MessageUtil(wsMsg);
        assertEquals(wsMsg.trim(), messageUtil.printMessage());
    }

    @Test
    public void testPrintMessagePrintsExpectedMessage() {
        System.out.println("Testing testPrintMessagePrintsExpectedMessage....");
        String msg2Print = "Print This Expected Message Please";
        assertEquals(msg2Print, messageUtil.printMessage(msg2Print));
    }
    
    @Test
    public void testDefaultConstructorIsCreatedWithDefaultMessage() {
        System.out.println("Testing testDefaultConstructorIsCreatedWithDefaultMessage....");
        
        String[] defaultMsgSnippets = {
            "Hi there!", "I'd greet you properly", 
            "You can run me with", "<your-name>"
        };
        MessageUtil messageUtil = new MessageUtil();
        String printedMsg = messageUtil.printMessage();

        assertThat(printedMsg, allOf(
            containsString(defaultMsgSnippets[0]),
            containsString(defaultMsgSnippets[1]),
            containsString(defaultMsgSnippets[2]),
            containsString(defaultMsgSnippets[3])
        ));
    }

    @Test
    public void testSalutationMessage(){
        System.out.println("Testing testSalutationMessage....");
        String who2Salute = "Peskileena";
        String expectedSalutationMsg = new StringBuilder()
            .append("Hi! ").append(who2Salute)
            .append(".... Nice to meet you!")
            .toString();
        
        assertEquals(expectedSalutationMsg, messageUtil.salutationMessage(who2Salute));
    }

}

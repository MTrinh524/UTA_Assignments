import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import poker.Hand;
import poker.Card;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class Assignment1Test 
{
    // Define some hands as json strings that can be used for many tests
    private final String four_5s = "{'cards':[{'suite':'SPADES','value':'FIVE'},{'suite':'DIAMONDS','value':'FIVE'},{'suite':'CLUBS','value':'FIVE'},{'suite':'HEARTS','value':'FIVE'},{'suite':'SPADES','value':'ACE'}]}";
    private final String three_5s = "{'cards':[{'suite':'SPADES','value':'FOUR'},{'suite':'DIAMONDS','value':'FIVE'},{'suite':'CLUBS','value':'FIVE'},{'suite':'HEARTS','value':'FIVE'},{'suite':'SPADES','value':'ACE'}]}";
    private final String royal_flush = "{'cards':[{'suite':'SPADES','value':'KING'},{'suite':'SPADES','value':'JACK'},{'suite':'SPADES','value':'QUEEN'},{'suite':'SPADES','value':'TEN'},{'suite':'SPADES','value':'ACE'}]}";
    private final String straight_flush = "{'cards':[{'suite':'DIAMOND','value':'JACK'},{'suite':'DIAMOND','value':'EIGHT'},{'suite':'DIAMOND','value':'QUEEN'},{'suite':'DIAMOND','value':'TEN'},{'suite':'DIAMOND','value':'NINE'}]}";
    private final String full_house = "{'cards':[{'suite':'SPADES','value':'KING'},{'suite':'DIAMONDS','value':'TEN'},{'suite':'CLUBS','value':'KING'},{'suite':'HEARTS','value':'TEN'},{'suite':'SPADES','value':'KING'}]}";
    private final String flush = "{'cards':[{'suite':'HEARTS','value':'FIVE'},{'suite':'HEARTS','value':'QUEEN'},{'suite':'HEARTS','value':'KING'},{'suite':'HEARTS','value':'NINE'},{'suite':'HEARTS','value':'THREE'}]}";
    private final String straight = "{'cards':[{'suite':'SPADES','value':'JACK'},{'suite':'DIAMONDS','value':'TEN'},{'suite':'CLUBS','value':'NINE'},{'suite':'HEARTS','value':'EIGHT'},{'suite':'SPADES','value':'SEVEN'}]}";
    private final String two_pair = "{'cards':[{'suite':'SPADES','value':'TWO'},{'suite':'CLUBS','value':'SIX'},{'suite':'HEARTS','value':'SIX'},{'suite':'HEARTS','value':'QUEEN'},{'suite':'SPADES','value':'QUEEN'}]}";
    private final String pair = "{'cards':[{'suite':'SPADES','value':'JACK'},{'suite':'CLUBS','value':'JACK'},{'suite':'HEARTS','value':'SIX'},{'suite':'HEARTS','value':'TWO'},{'suite':'SPADES','value':'SEVEN'}]}";
    private final String high_card = "{'cards':[{'suite':'SPADES','value':'FOUR'},{'suite':'DIAMONDS','value':'FIVE'},{'suite':'CLUBS','value':'SEVEN'},{'suite':'HEARTS','value':'TWO'},{'suite':'SPADES','value':'ACE'}]}";

    //Use these to check how the comparisons work if they are the same type of poker hand
    private final String four_4s = "{'cards':[{'suite':'SPADES','value':'FOUR'},{'suite':'DIAMONDS','value':'FOUR'},{'suite':'CLUBS','value':'FOUR'},{'suite':'HEARTS','value':'FOUR'},{'suite':'SPADES','value':'ACE'}]}";
    private final String two_jacks = "{'cards':[{'suite':'SPADES','value':'TWO'},{'suite':'CLUBS','value':'SIX'},{'suite':'HEARTS','value':'SIX'},{'suite':'HEARTS','value':'JACK'},{'suite':'SPADES','value':'JACK'}]}";
    private final String same_flush = "{'cards':[{'suite':'HEARTS','value':'FIVE'},{'suite':'HEARTS','value':'QUEEN'},{'suite':'HEARTS','value':'KING'},{'suite':'HEARTS','value':'NINE'},{'suite':'HEARTS','value':'THREE'}]}";
    private final String king_high_card = "{'cards':[{'suite':'SPADES','value':'FOUR'},{'suite':'DIAMONDS','value':'FIVE'},{'suite':'CLUBS','value':'SEVEN'},{'suite':'HEARTS','value':'TWO'},{'suite':'SPADES','value':'QUEEN'}]}";

    private static final Logger LOGGER = LogManager.getLogger(Assignment1Test.class);

    
    @Test
    void four_of_a_kind_better_then_3_of_a_kind() 
    {
        // Use the logger to see what is happening 
        // with a test when it fails.  it is writen
        // to a log file.

        LOGGER.debug(" in the 4 of a kind test");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(four_5s,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(three_5s,Hand.class);

        assertTrue(H1.is_better_than(H2));
    }

    @Test
    void royal_flush_better_than_straight_flush()
    {
        LOGGER.debug(" in the royal flush test");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(royal_flush,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(straight_flush,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    @Test
    void four_5s_better_than_four_4s()
    {
        LOGGER.debug(" in the both hands have 4 of a kind test -- four 5s is better");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(four_5s,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(four_4s,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    @Test
    void two_queens_better_than_two_jacks()
    {
        LOGGER.debug(" in the both hands have two-pair test -- 2 queens is better");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(two_pair,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(two_jacks,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    @Test
    void flush_are_equal()
    {
        LOGGER.debug(" in the both flushes are equal test");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(flush,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(same_flush,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    @Test
    void flush_is_better_than_straight()
    {
        LOGGER.debug(" in the flush test");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(flush,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(straight,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    @Test
    void pair_better_than_high_card()
    {
        LOGGER.debug(" in the pair test");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(pair,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(high_card,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    @Test
    void full_house_better_than_three_of_a_kind()
    {
        LOGGER.debug(" in the full house test");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(full_house,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(three_5s,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    void ace_high_card_better_than_king_high_card()
    {
        LOGGER.debug(" in the both hands are high cards test -- Ace high card is better");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(high_card,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(king_high_card,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }

    void straight_better_than_pair()
    {
        LOGGER.debug(" in the straight test");

        // turn it into json
        Gson gson = new Gson();
        Hand H1 = new Hand();
        H1 = gson.fromJson(straight,Hand.class);
        Hand H2 = new Hand();
        H2 = gson.fromJson(pair,Hand.class);
        
        assertTrue(H1.is_better_than(H2));
    }




}

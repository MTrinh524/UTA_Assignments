package poker;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import poker.Card;

public class Hand
{
    //private transient int i=10;
    // marked transient they will not serialized / deserialized

    public Card[] cards;
    final transient int maxRank = 14;
    transient int score = 0, score1, score2;
    transient int sCount = 0, vCount = 0;

    public Hand()
    {
    }

    public int royalFlush()
    {
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].suite == cards[x].suite)
            {
                sCount++;
            }
            if(toInt(cards[x-1].value.toString()) == maxRank-(x-1))
            {
                vCount++;
            }
            if(sCount == 5 && vCount == 5)
            {
                score = 10;
            }
        }
        return score;
    }

    public int straightFlush()
    {
        sCount = 0;
        vCount = -1;
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].suite == cards[x].suite)
            {
                sCount++;
            }
            if(toInt(cards[0].value.toString()) != maxRank && toInt(cards[x-1].value.toString()) == toInt(cards[x].value.toString())+1 )
            {
                vCount++;
            }
            if(sCount == 5 && vCount == 4)
            {
                score = 9;
            }
        }    
        return score;  
    }

    public int fourofaKind()
    {
        sCount = 0;
        vCount = 0;
        for(int x = 1; x <= 4; x++)
        {
            if(cards[x-1].value == cards[x].value)
            {
                vCount++;
                sCount++;
            }
            if(sCount == 4 && vCount == 4)
            {
                score = 8;
            }
        }
        return score;
    }

    public int fullHouse()
    {
        sCount = 0;
        vCount = 0;
        for(int x = 1; x < 3; x++)
        {
            if(cards[x-1].value == cards[x].value)
            {
                vCount++;
                sCount++;
            }
        }
        if(cards[3].value == cards[4].value)
        {
            vCount++;
        }
        if(vCount == 4 && sCount == 3)
        {
            score = 7;
        }
        return score;
    }

    public int flush()
    {
        sCount = 0; 
        vCount = 0;
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].value != cards[x].value)
            {
                vCount++;
            }
            else if(cards[x-1].suite == cards[x].suite)
            {
                sCount = 1;
            }
            else
            {
                sCount = 0;
            }
            if(vCount == 5 && sCount == 1)
            {
                score = 6;
            }
        }
        return score;
    }

    public int straight()
    {
        sCount = 0;
        vCount = 0;
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].suite == cards[x].suite)
            {
                sCount++;
            }
            if(toInt(cards[0].value.toString()) != maxRank && toInt(cards[x-1].value.toString()) == toInt(cards[x].value.toString())+1 )
            {
                vCount++;
            }
            if(sCount != 5 && vCount == 4)
            {
                score = 5;
            }
        }
        return score;
    }

    public int threeofaKind()
    {
        sCount = 0;
        vCount = 0;
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].value == cards[x].value)
            {
                vCount++;
            }
            if(cards[3].value != cards[4].value)
            {
                sCount = 1;
            }
            if(sCount == 1 && vCount == 3)
            {
                score = 4;
            }
        }
        return score;
    }

    public int twoPair()
    {
        sCount = 0;
        vCount = 0;
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].value == cards[x].value)
            {
                vCount++;
            }
            if(cards[4].value != cards[4].value)
            {
                sCount = 1;
            }
            if(sCount == 1 && vCount == 2)
            {
                score = 3;
            }
        }
        return score;
    }

    public int pair()
    {
        sCount = 0;
        vCount = 0;
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].value == cards[x].value)
            {
                vCount++;
            }
            if(cards[2].value != cards[2].value)
            {
                sCount = 1;
            }
            if(sCount == 1 && vCount == 1)
            {
                score = 2;
            }
        }
        return score;
    }

    public int highCard()
    {
        sCount = 0;
        vCount = 0;
        for(int x = 1; x < 5; x++)
        {
            if(cards[x-1].value == cards[x].value)
            {
                vCount++;
            }
            if(cards[x-1].suite == cards[x].suite)
            {
                sCount++;
            }
            if(sCount == 0 && vCount == 0)
            {
                score = 1;
            }
        }
        return score;
    }

    public boolean is_better_than(Hand H)
    {

        //Sorts the cards from biggest to smallest by face value
        sort(); 
        H.sort();
        
        //Royal Flush
        score1 = royalFlush();
        score2 = H.royalFlush();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else if(score1 == 10 && score2 == 10)
        {
            return false;
        }

        //Straight Flush
        score1 = straightFlush();
        score2 = H.straightFlush();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 9 && score2 == 9)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
        }

        //Four-of-a-kind
        score1 = fourofaKind();
        score2 = H.fourofaKind();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 8 && score2 == 8)
            {
            return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
            else if(toInt(H.cards[0].value.toString()) == toInt(cards[0].value.toString()))
            {
                if(toInt(H.cards[4].value.toString()) > toInt(cards[4].value.toString()))
                {
                    return false;
                }
                else if(toInt(H.cards[4].value.toString()) < toInt(cards[4].value.toString()))
                {
                    return true;
                }
            }
        }

        //Full House
        score1 = fullHouse();
        score2 = H.fullHouse();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 7 && score2 == 7)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
            else if(toInt(H.cards[0].value.toString()) == toInt(cards[0].value.toString()))
            {
                if(toInt(H.cards[3].value.toString()) > toInt(cards[3].value.toString()))
                {
                    return false;
                }
                else if(toInt(H.cards[3].value.toString()) < toInt(cards[3].value.toString()))
                {
                    return true;
                }
            }
        }

        //Flush
        score1 = flush();
        score2 = H.flush();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 6 && score2 == 6)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
        }

        //Straight
        score1 = straight();
        score2 = H.straight();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 5 && score2 == 5)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
        }

        //Three-of-a-kind
        score1 = threeofaKind();
        score2 = H.threeofaKind();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 4 && score2 == 4)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
            else if(toInt(H.cards[0].value.toString()) == toInt(cards[0].value.toString()))
            {
                if(toInt(H.cards[3].value.toString()) > toInt(cards[3].value.toString()))
                {
                    return false;
                }
                else if(toInt(H.cards[3].value.toString()) < toInt(cards[3].value.toString()))
                {
                    return true;
                }
                else if(toInt(H.cards[3].value.toString()) == toInt(cards[3].value.toString()))
                {
                    if(toInt(H.cards[4].value.toString()) > toInt(cards[4].value.toString()))
                    {
                        return false;
                    }
                    else if(toInt(H.cards[4].value.toString()) < toInt(cards[4].value.toString()))
                    {
                        return true;
                    }
                }
            }
        }

        //Two-pair
        score1 = twoPair();
        score2 = H.twoPair();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 3 && score2 == 3)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
            else if(toInt(H.cards[0].value.toString()) == toInt(cards[0].value.toString()))
            {
                if(toInt(H.cards[2].value.toString()) > toInt(cards[2].value.toString()))
                {
                    return false;
                }
                if(toInt(H.cards[2].value.toString()) < toInt(cards[2].value.toString()))
                {
                    return true;
                }
                else if(toInt(H.cards[2].value.toString()) == toInt(cards[2].value.toString()))
                {
                    if(toInt(H.cards[4].value.toString()) > toInt(cards[4].value.toString()))
                    {
                        return false;
                    }
                    else if(toInt(H.cards[4].value.toString()) < toInt(cards[4].value.toString()))
                    {
                        return true;
                    }
                }
            }
        }

        //Pair
        score1 = pair();
        score2 = H.pair();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 2 && score2 == 2)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
            else if(toInt(H.cards[0].value.toString()) == toInt(cards[0].value.toString()))
            {
                if(toInt(H.cards[2].value.toString()) > toInt(cards[2].value.toString()))
                {
                    return false;
                }
                else if(toInt(H.cards[2].value.toString()) < toInt(cards[2].value.toString()))
                {
                    return true;
                }
            }
        }

        //High card
        score1 = highCard();
        score2 = H.highCard();
        if(score1 < score2)
        {
            return false;
        }
        else if(score1 > score2)
        {
            return true;
        }
        else
        {
            if(toInt(H.cards[0].value.toString()) > toInt(cards[0].value.toString()) && score1 == 1 && score2 == 1)
            {
                return false;
            }
            else if(toInt(H.cards[0].value.toString()) < toInt(cards[0].value.toString()))
            {
                return true;
            }
        }

        return true;
    }

    //sorts the cards from biggest to smallest by face value
    public void sort()
    {
        int x, y, max;
        Card temp;
        for(x = 0; x < 5; x++)
        {
            max = x;
            for(y = x+1; y < 5; y++)
            {
                if( toInt(cards[y].value.toString()) >  toInt(cards[max].value.toString()))
                {
                    max = y;
                }
            }
            temp = cards[x];
            cards[x] = cards[max];
            cards[max] = temp;
        }
    }

    //assigns values to the string literal of the face card
    public int toInt(String value)
    {
        int rank = 0;
        switch(value)
        {
            case "TWO": 
                rank = 2;
                break;
            case "THREE": 
                rank = 3;
                break;
            case "FOUR": 
                rank = 4;
                break;
            case "FIVE": 
                rank = 5;
                break;
            case "SIX": 
                rank = 6;
                break;
            case "SEVEN": 
                rank = 7;
                break;
            case "EIGHT": 
                rank = 8;
                break;
            case "NINE": 
                rank = 9;
                break;
            case "TEN": 
                rank = 10;
                break;
            case "JACK": 
                rank = 11;
                break;
            case "QUEEN": 
                rank = 12;
                break;
            case "KING": 
                rank = 13;
                break;
            case "ACE": 
                rank = 14;
                break;
        }
        return rank;
    }
   
   public boolean is_equal(Hand H)
   {
       if(H.cards == cards)
       {
           return true;
       }

       return false;
   }
}

"""
Codemonk link: https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/the-final-fight-6/

Fatal Eagle has had it enough with Arjit aka Mr. XYZ who's been trying to destroy the city from the first go. He cannot
tolerate all this nuisance anymore. He's... tired of it. He decides to get rid of Arjit and his allies in a war. He
knows that Arjit has N people fighting for him, so he brings his own N people in the war to face him. (So, there will
be 2 * N people fighting in this war!). He knows for him to win the war against his enemy, members of his army should be
present before the members of Arjit come up in the battlefield - that is to say, whenever a member of Arijt's army comes
in the battlefield, there should already be a member of his own army there to handle him. (In short, the number of his
army members should never be less than the number of Arjit's army members in the field!). If he figures out the number
of ways such such sequences can be formed, the good will be able to conquer evil yet again. Help Fatal Eagle in figuring
it out to defeat Arjit - once and for all.

Input - Output:
There is only one integer in the only line of the input, denoting the value of N.
Print the number of valid sequences. Since the output might be very big, print it
modulo 10^9+9.

Sample input:
3

Sample Output:
5
"""

"""
That's a pure math's problem. The total amount of combinations if we could place the first army wherever we wanted,
would be the combinations of picking N out of 2*N positions. 2*N are the total soldiers of both armies. That can be
easily calculated by our logic, or, if we already understand the logic behind it, we can directly use the binomial
coefficient. From the total amount of combinations we must subtract those that are invalid. How many are those? The 
answer is bionomial(2n, n+1). If we make the total calculation, we derive the catalan number.

1) bionimial(2n, n+1) = n/(n+1)*bionimial(2n, n). The proof is very easy.
2) bionimial(2n, n) - (bionimial(2n, n+1) = bionimial(2n, n) - n/(n+1)*bionimial(2n, n)
   = bionimial(2n, n) * [1-n/(n+1)] = 1/(n+1) * bionimial(2n, n) = 1/(n+1) * (2n)!/(n!n!)
   
The above explanation is not THAT straight forward. Another, better way to understand the derivation of the catalan 
number and the one suggested has been proven in the paper of Rukavicka Josef (2011). Just to give a brief spoil, the 
catalan number is: 1/(n+1) * bionomial(2n, n). It's like we split the bionomial term in n+1 equal parts and the answer
is one of them!! 

Since our mod is a prime number, we can calculate using the Fermat's little theorem the modulo inverse for n! and n+1
and make the calculation easier.

O(logN) for the exponentiations and O(N) for the factorizations.

Final complexity: O(N)
"""


def exponentiate(number, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (number * result) % mod

        number = (number ** 2) % mod
        exponent //= 2
    return result


def factorial(number):
    temp = 1
    for i in range(1, number+1):
        temp = (temp*i) % mod

    return temp


n = int(input())
mod = 1000000009

a = factorial(2*n)
b = exponentiate(factorial(n), mod-2)
c = exponentiate(n+1, mod-2)
answer = (a*b*b*c) % mod

print(answer)

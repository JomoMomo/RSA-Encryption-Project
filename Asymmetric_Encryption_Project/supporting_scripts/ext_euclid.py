''' 
Solving for x in -- ax + by = 1 -- is equivelant to finding x in -- ax ≡ 1(mod b) 
                                                               -- ax-1 ≡ 0(mod b)
                                                               -- ax-1 ≡ yb  -for some integer b
                                                               -- ax-by = 1
                                                               -- ax+b(-y) = 1 since we don't care about y or its sign
                                                               -- Hence EEA can be used to solve for x.
                                                               -- BELOW WE SOLVE FOR x AND y BY s[-2]=x AND t[-2]=y ---> s[i]*a + t[i]*b = r
The purpose of this is that when we replace a with e, b with phi, and solvr for x as our d, we can use this to create our private key d (decryptor)
The above holds true only when a and b are relatively prime, which holds for any and all pairs of prime numbers.
 '''

def xgcd(e,phi):
    original_e = e
    original_phi = phi
    #e, phi = max(e,phi), min(e,phi)


    q=[1,-1]
    r=[e,phi]
    s=[1,0]
    t=[0,1]

    while r[-1] > 0:
        q.append(r[-2] // r[-1])    # Doing the quotient of the last two r
        r.append(r[-2] % r[-1])     # Doing the remainder of the last two r
        s.append(s[-2] - q[-1] * s[-1])
        t.append(t[-2] - q[-1] * t[-1])

        d = s[-2]
        if d > 0:
            d = d+original_phi 
        elif d < 0:
            d = d + 2*original_phi
    return d # we only care about the 'x' because that is what is equivelant to 'd' when soling for the decrypion (private) key

# Equivelance: 
#   e*d = 1(mod(phi)) 
#   e*d + (mod(phi))y = 1 (where y is a dummy variable)
#   so to solve for d using the above function, you would run:
#   xgcd(e,phi)
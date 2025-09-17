import random

from deprecated import deprecated


class float_point:
    def __init__(self):
        pass

    def vf_question(self, number=0):
        """generate random question"""
        if number:
            return number
        x = round(random.uniform(12, 256), 3)
        sign = random.choice([-1, 1])
        x = x * sign
        return x

    @staticmethod
    def decimal_converter(num):
        while num > 1:
            num /= 10.0
        return num

    # Function for converting decimal to binary
    def float_bin(self, number, places=3):
        try:
            whole, dec = str(number).split(".")
        except:
            whole = number
            dec = 0
        whole = int(whole)
        dec = int(dec)
        res = bin(whole).lstrip("0b") + "."

        for x in range(places):
            try:
                whole, dec = str((self.decimal_converter(dec)) * 2).split(".")
            except:
                whole = self.decimal_converter(dec) * 2
                dec = 0
            dec = int(dec)
            res += str(whole)
        return res

    #
    # @deprecated(reason="Use ieee754_components(n) instead.")
    # def IEEE754(self, n, method=False):
    #
    #     # identifying whether the number
    #     # is positive or negative
    #     sign = 0
    #     if n < 0:
    #         sign = 1
    #         n = n * (-1)
    #     p = 30
    #
    #     # convert float to binary
    #     dec = self.float_bin(n, places=p)
    #     text = ""
    #     text += "%.4f = %s\n" % (n, dec)
    #     # separate the decimal part
    #     # and the whole number part
    #     whole, dec = str(dec).split(".")
    #     whole = int(whole)
    #
    #     # calculating the exponent(E)
    #     exponent = len(str(whole)) - 1
    #     exponent_bits = 127 + exponent
    #
    #     # converting the exponent from
    #     # decimal to binary
    #     exponent_bits = bin(exponent_bits).lstrip("0b")
    #
    #     # finding the mantissa
    #     mantissa = str(whole)[1 : exponent + 1]
    #     mantissa = mantissa + dec
    #     mantissa = mantissa[0:23]
    #
    #     # the IEEE754 notation in binary
    #     final = str(sign) + str(exponent_bits) + mantissa
    #
    #     # convert the binary to hexadecimal
    #     hstr = "%0*X" % ((len(final) + 3) // 4, int(final, 2))
    #
    #     # ~ text =""
    #     text += " Forme normalise 1.%s x2\^%d\n" % (mantissa, exponent)
    #     if n < 0:
    #         text += "Signe - => 1\n"
    #     else:
    #         text += "Signe + => 0\n"
    #
    #     text += " exposant %d +127 = %d =(%s)\n " % (
    #         exponent,
    #         exponent + 127,
    #         exponent_bits,
    #     )
    #
    #     text += " pseudo mantisse  %s \n" % (mantissa)
    #     text += " La representation \n %s\n" % final
    #     text += " Hex %s\n" % hstr
    #     if method:
    #         return text
    #     # return the answer to the driver code
    #     else:
    #         return hstr

    def ieee754_components(self, n):
        """
        Extracts components needed for IEEE-754 32-bit representation.
        Returns a dictionary with all intermediate and final values.
        """
        original = n
        sign = 0
        if n < 0:
            sign = 1
            n = -n

        p = 30
        binary_repr = self.float_bin(n, places=p)

        whole, dec = str(binary_repr).split(".")
        whole = int(whole)

        exponent = len(str(whole)) - 1
        exponent_raw = 127 + exponent
        exponent_bits = bin(exponent_raw).lstrip("0b")

        mantissa = str(whole)[1 : exponent + 1] + dec
        mantissa = mantissa[:23]

        final_binary = f"{sign}{exponent_bits}{mantissa}"
        hex_repr = "%0*X" % ((len(final_binary) + 3) // 4, int(final_binary, 2))

        return {
            "number": original,
            "abs_value": n,
            "sign": sign,
            "binary_repr": binary_repr,
            "exponent": exponent,
            "exponent_raw": exponent_raw,
            "exponent_bits": exponent_bits,
            "mantissa": mantissa,
            "final_binary": final_binary,
            "hex": hex_repr,
        }


# Driver Code
if __name__ == "__main__":
    vf = float_point()
    print(vf.IEEE754(263.3))
    print(vf.IEEE754(-263.3))
    vf.vf_question()

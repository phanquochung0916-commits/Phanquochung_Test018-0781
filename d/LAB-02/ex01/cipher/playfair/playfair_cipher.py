class PlayFairCipher:

    def __init__(self):
        pass

    def create_playfair_matrix(self, key):

        key = key.upper().replace("J", "I")

        used = set()
        matrix_chars = []

        # thêm key vào matrix
        for ch in key:
            if ch.isalpha() and ch not in used:
                used.add(ch)
                matrix_chars.append(ch)

        # thêm alphabet còn thiếu
        for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if ch not in used:
                used.add(ch)
                matrix_chars.append(ch)

        # tạo ma trận 5x5
        matrix = [matrix_chars[i:i+5] for i in range(0, 25, 5)]

        return matrix

    def find_letter_coords(self, matrix, letter):

        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col

        raise ValueError(f"Character '{letter}' not found in matrix")

    def prepare_text(self, text):

        text = text.upper().replace("J", "I")

        # bỏ ký tự không phải alphabet
        text = ''.join(ch for ch in text if ch.isalpha())

        result = ""
        i = 0

        while i < len(text):

            a = text[i]

            if i + 1 < len(text):
                b = text[i + 1]

                # nếu 2 ký tự giống nhau
                if a == b:
                    result += a + "X"
                    i += 1
                else:
                    result += a + b
                    i += 2
            else:
                result += a + "X"
                i += 1

        return result

    def playfair_encrypt(self, plain_text, matrix):

        plain_text = self.prepare_text(plain_text)

        encrypted_text = ""

        for i in range(0, len(plain_text), 2):

            a = plain_text[i]
            b = plain_text[i + 1]

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            # cùng hàng
            if row1 == row2:

                encrypted_text += (
                    matrix[row1][(col1 + 1) % 5] +
                    matrix[row2][(col2 + 1) % 5]
                )

            # cùng cột
            elif col1 == col2:

                encrypted_text += (
                    matrix[(row1 + 1) % 5][col1] +
                    matrix[(row2 + 1) % 5][col2]
                )

            # hình chữ nhật
            else:

                encrypted_text += (
                    matrix[row1][col2] +
                    matrix[row2][col1]
                )

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):

        cipher_text = cipher_text.upper()

        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):

            a = cipher_text[i]
            b = cipher_text[i + 1]

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            # cùng hàng
            if row1 == row2:

                decrypted_text += (
                    matrix[row1][(col1 - 1) % 5] +
                    matrix[row2][(col2 - 1) % 5]
                )

            # cùng cột
            elif col1 == col2:

                decrypted_text += (
                    matrix[(row1 - 1) % 5][col1] +
                    matrix[(row2 - 1) % 5][col2]
                )

            # hình chữ nhật
            else:

                decrypted_text += (
                    matrix[row1][col2] +
                    matrix[row2][col1]
                )

        return decrypted_text
class RailFenceCipher:
    def rail_fence_encrypt(self, plain_text, num_rails):

        if num_rails <= 1:
            return plain_text

        rails = [[] for _ in range(num_rails)]

        rail_index = 0
        direction = 1

        for char in plain_text:
            rails[rail_index].append(char)

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        return ''.join(''.join(r) for r in rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):

        if num_rails <= 1:
            return cipher_text

        pattern = []

        rail_index = 0
        direction = 1

        # tạo pattern đi xuống / đi lên
        for _ in range(len(cipher_text)):
            pattern.append(rail_index)

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        # đếm số ký tự mỗi rail
        rail_counts = [0] * num_rails
        for r in pattern:
            rail_counts[r] += 1

        # chia cipher_text vào từng rail
        rails = []
        idx = 0
        for count in rail_counts:
            rails.append(list(cipher_text[idx:idx + count]))
            idx += count

        # rebuild plaintext
        result = []
        rail_pos = [0] * num_rails

        for r in pattern:
            result.append(rails[r][rail_pos[r]])
            rail_pos[r] += 1

        return ''.join(result)
class MaxHeap:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        index = len(self.values) - 1

        while index > 0:
            parent = (index - 1) // 2
            if self.values[parent] >= self.values[index]:
                break
            self.values[parent], self.values[index] = self.values[index], self.values[parent]
            index = parent

    def extract_max(self):
        if not self.values:
            raise IndexError("堆積是空的")

        maximum = self.values[0]
        last = self.values.pop()
        if self.values:
            self.values[0] = last
            self._sift_down(0)
        return maximum

    def _sift_down(self, index):
        size = len(self.values)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.values[left] > self.values[largest]:
                largest = left
            if right < size and self.values[right] > self.values[largest]:
                largest = right
            if largest == index:
                break

            self.values[index], self.values[largest] = self.values[largest], self.values[index]
            index = largest

    def show_tree(self):
        if not self.values:
            return "堆積是空的"

        lines = []
        start = 0
        width = 1
        level = 1
        while start < len(self.values):
            end = min(start + width, len(self.values))
            lines.append(f"第 {level} 層：{' '.join(map(str, self.values[start:end]))}")
            start = end
            width *= 2
            level += 1
        return "\n".join(lines)

    def show_complexity(self):
        return (
            "堆積排序時間複雜度：O(n log n)（最佳、平均、最差）\n"
            "原地堆積排序額外空間：O(1)\n"
            "本程式儲存堆積資料的空間：O(n)\n"
            "本程式每次插入或取出最大值：O(log n)"
        )

def main():
    heap = MaxHeap()
    print("=== 最大堆積二元樹 ===")

    while True:
        print("\n1. 插入數值  2. 取出最大值  3. 顯示堆積  4. 複雜度資訊  5. 結束")
        choice = input("請選擇：").strip()

        if choice == "1":
            try:
                value = int(input("請輸入整數："))
            except ValueError:
                print("請輸入有效的整數")
                continue
            heap.insert(value)
            print(f"已插入 {value}")
            print(heap.show_tree())
        elif choice == "2":
            try:
                print(f"取出的最大值：{heap.extract_max()}")
            except IndexError as error:
                print(error)
            print(heap.show_tree())
        elif choice == "3":
            print(heap.show_tree())
            print(f"陣列表示：{heap.values}")
        elif choice == "4":
            print(heap.show_complexity())
        elif choice == "5":
            break
        else:
            print("請輸入 1 到 5")


if __name__ == "__main__":
    main()
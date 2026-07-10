class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'D':
                tmp = record[-1] * 2
                record.append(tmp)
            elif operation == 'C':
                record.pop()
            else:
                record.append(int(operation))

        
        return sum(record)
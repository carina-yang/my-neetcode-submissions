class Solution:

    def _isInteger(self, string) -> bool:
        return string.isdigit() or (string[0] == '-' and string[1:].isdigit())

    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            if self._isInteger(operation):
                record.append(int(operation))
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'D':
                tmp = record[-1] * 2
                record.append(tmp)
            elif operation == 'C':
                record.pop()
        
        return sum(record)
import csv

mapping = dict()
needed = ['approver', 'state', 'approval_source', 'sys_updated_on']

def make_mapping():
    with open('t2.csv') as table2:
        csv_reader = csv.reader(table2, delimiter=',')
        match = ['sysapproval', 'state']
        rev_map = dict()
        begin = True
        for row in csv_reader:
            if begin:
                cnt = 0
                begin = False
                for col in row:
                    rev_map[col] = cnt
                    cnt += 1    
            else:
                idx1 = rev_map[match[0]]
                idx2 = rev_map[match[1]]
                val1 = row[idx1]
                val2 = row[idx2]
                if val2 != 'approved':
                    continue
                if val1 not in mapping:
                    mapping[val1] = dict()
                    for ele in needed:
                        idx = rev_map[ele]
                        val = row[idx]
                        mapping[val1][ele] = val

def in_date_range(val):
    return False

def merge_tables():
    with open('vigz_output.csv', mode='w') as out_file:
        out_file_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open('t1.csv') as table1:
            csv_reader = csv.reader(table1, delimiter=',')
            match = ['sys_id', 'OPENED_TS']
            rev_map = dict()
            begin = True
            for row in csv_reader:
                if begin:
                    cnt = 0
                    begin = False
                    for col in row:
                        rev_map[col] = cnt
                        cnt += 1  
                    for ele in needed:
                        row.append(ele) 
                else:
                    idx1 = rev_map[match[0]]
                    idx2 = rev_map[match[1]]
                    val1 = row[idx1]
                    val2 = row[idx2]
                    if not in_date_range(val2):
                        continue
                    if val1 in mapping:
                        for ele in needed:
                            row.append(mapping[val1][ele])
                out_file_writer.writerow(row) 


if __name__ == '__main__':
    make_mapping()
    merge_tables()



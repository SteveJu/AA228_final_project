import subprocess
import json

for i in range(1000):
    print('Starting to process ' + str(i) + '.py')
    infile = open('outputs/codes/' + str(i) + '.json')
    code = json.load(infile)
    with open('outputs/processed_code/' + str(i) + '.py', 'w') as f:
        for line in code[str(i)]['code']:
            try:
                f.write(line)
            except:
                f.write('# Error lines\n')
        f.close()
    file_name = 'outputs/processed_code/' + str(i) + '.py'
    result = subprocess.run(["pylint", file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    with open('outputs/pylint_results/pylint_result_' + str(i) + '.txt', 'w') as outfile:
        outfile.write(output)
        outfile.close()

    print('Finished to process pylint_result_' + str(i) + '.txt\n')

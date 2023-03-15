import subprocess
import json

d = 'train/'

for i in range(1000):
    print('Starting to process ' + str(i) + '.py\n')
    infile = open(d + 'codes/' + str(i) + '.json')
    code = json.load(infile)
    for j in range(10):
        with open(d + 'processed_code/' + str(i) + '_' + str(j) + '.py', 'w') as f:
            for line in code[str(i)]['code'][j]:
                try:
                    f.write(line)
                except:
                    f.write('# Error lines\n')
            f.close()
        file_name = d + 'processed_code/' + str(i) + '_' + str(j) + '.py'
        result = subprocess.run(["pylint", file_name, "--disable=C,W0311"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode("utf-8")

        with open(d + 'pylint_results/pylint_result_' + str(i) + '_' + str(j) + '.txt', 'w') as outfile:
            outfile.write(output)
            outfile.close()

        score = ''
        if 'syntax-error' in output:
            score = 'syntax-error'
        elif 'parse-error' in output:
            score = 'parse-error'
        else:
            start_idx = output.index('Your code has been rated at ')
            end_idx = output.index('/10')
            score = output[start_idx + 28: end_idx]
        s = str(i) + '_' + str(j) + ': ' + score
        with open(d + 'pylint_scores/overall.txt', 'a') as outfile3:
            outfile3.write(s + '\n')
            outfile3.close()
        # with open(d + 'pylint_scores/pylint_scores_' + str(i) + '_' + str(j) + '.txt', 'w') as outfile2:
        #     outfile2.write(score)
        #     outfile2.close()

        print('Finished to process pylint_result_' + str(i) + '_' + str(j) + '.txt\n')



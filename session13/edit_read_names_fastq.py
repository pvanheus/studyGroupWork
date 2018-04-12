import click

@click.command()
@click.argument('data')
def change_readnames(data):
  """ Adds "\1" or "\2" to paired end read names in fastq file generated by
  Illumina Hiseq. This format is needed for input for Trans-ABySS"""

  # read in original fastq file
  f = open(data)
  # fastq = f.readlines()

  # remove new line characters
  # L = []
  # for line in f:
  #   line = line.rstrip() # remove \n characters for accurate count
  #   L.append(line)

  # add "\1" to the end of the read name lines
  count = 0
  output_file = open('sequence_new.fq', 'w') # change 'sequence_new.fq' to the name you want for your new fastq file
  for line in f:
    if line.startswith("@"):
        changed_string = line + "\\1\n" # to add to reverse fastq change "\x01" to "\x02"
        output_file.write(changed_string)
        count += 1
    else:
        output_file.write(line)
  output_file.close()

    # re-add new line characters
    # final = []
    # for line in fastq_new:
    #     line += "\n"
    #     final.append(line)

    # write to file
    # output_file.writelines(fastq_new)
    # output_file.close()
  print(count, "reads in", data)

if __name__ == '__main__':
      change_readnames()

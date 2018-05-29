# xmlspy
This module itends to group xml files by type (CTE or NFE) and version (1.04, 2.00, 3.10)

# xmlspy (PT-BR)
Esse módulo busca agrupar arquivos xml por tipo (CTE ou NFE) e versão (1.04, 2.00, 3.10)

## main()

A função main lida com o recebimento de argumentos do usuário e com a iteração recursiva do caminho do diretório fornecido.
O método os.walk() percorre a **árvore de diretórios** a partir da **raiz** fornecida pelo usuário, do topo para baixo.

Exemplo básico:

```
>>> import os                                                                                                        
>>> walk = os.walk("C:\\Users\\vitor.rabelo\\Documents\\projetos_automatizacao\\oswalk_sample")                      
>>> walk                                                                                                             
<generator object walk at 0x000001D7E5FE4AF0>                                                                        
>>> next(walk)                                                                                                       
('C:\\Users\\vitor.rabelo\\Documents\\projetos_automatizacao\\oswalk_sample', ['A', 'B', 'C'], ['exemplo.txt'])      
>>> next(walk)                                                                                                       
('C:\\Users\\vitor.rabelo\\Documents\\projetos_automatizacao\\oswalk_sample\\A', ['1'], ['a.txt', 'aa.txt'])         
>>> next(walk)                                                                                                       
('C:\\Users\\vitor.rabelo\\Documents\\projetos_automatizacao\\oswalk_sample\\A\\1', [], ['1.txt'])                   
>>> next(walk)                                                                                                       
('C:\\Users\\vitor.rabelo\\Documents\\projetos_automatizacao\\oswalk_sample\\B', [], ['b.txt', 'bb.txt', 'bbb.txt']) 
>>> next(walk)                                                                                                       
('C:\\Users\\vitor.rabelo\\Documents\\projetos_automatizacao\\oswalk_sample\\C', [], ['c.txt', 'cc.txt', 'ccc.txt']) 
>>> next(walk)                                                                                                       
Traceback (most recent call last):                                                                                   
  File "<stdin>", line 1, in <module>                                                                                
StopIteration
```

## xml_path_handler(xml_dir_path)

Recebe o caminho do diretório que contém os arquivos xml a serem processados (dentro da própria pasta, ou em sub-pastas)
A função então irá garantir que apenas arquivos de extensão XML serão processados, ela imprimi o número de arquivos XML lidos para posterior
verificação e devolve uma **lista** contendo todos os nomes de arquivos XML lidos.

## xml_version_parser(list_of_xml_files, xml_dir_path):

Recebe a lista da função anterior e o caminho do diretório que contém os arquivos xml. Ele lê cada arquivo, identifica o tipo e versão e separa cada arquivo de acordo com esses critérios mencionados. A separação ocorre da seguinte forma: a função cria um diretório de nome ```xmlspy_<tipo>_<versão>``` e cópia os arquivos correspondentes para dentro da pasta.
A função também evita a possibilidade de criar pastas repetidas caso seja rodado novamente.

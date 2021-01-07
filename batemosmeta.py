# Esse script verifica se batemos as metas, perguntando ao usuário o quanto alcançamos e quais eram as metas iniciais
print('Vamos ver como estão as nossas metas...'  )

def metaInscritosCanalYoutube(quantidade):
  metaInscritos = int (input ('Qual é a meta de inscritos para o nosso Canal do Youtube Hoje?  '))
  meta_calculada = metaInscritos - qtdeInscritosCanal

  if qtdeInscritosCanal >= metaInscritos:
    print('Meta de inscritos no canal do Youtube alcançada com sucesso!')
    bateuMetaInscritosYoutube=1

  else: 
    print('Meta de inscritos no canal do Youtube ainda não alcançada. Faltam ', meta_calculada, ' novos inscritos.'  )
    bateuMetaInscritosYoutube=0
  return bateuMetaInscritosYoutube

def verificaLikesVideoYoutube(qtdeLikeVideo):
  metaLikesVideoYoutube = int (input ('Qual é a meta de Likes para o nosso Vídeo do Youtube Hoje?  '))
  faltaMetalikes=metaLikesVideoYoutube-qtdeLikeVideo;

  if qtdeLikeVideo >= metaLikesVideoYoutube:
    print('Meta likes no vídeo do Youtube alcançada com sucesso!')
    bateuMetaLikeVideoYoutube=1

  else: 
    print('Meta de likes no vídeo do Youtube ainda não alcançada. Ainda faltam ', faltaMetalikes, 'novos likes'  )
    bateuMetaLikeVideoYoutube=0
  return bateuMetaLikeVideoYoutube

def verificaCompartilhamento(qtdeCompartilhamento):
  metaCompartilhamentos = int (input ('Qual é a meta de Compartilhamentos para o nosso Vídeo de Ontem?  '))
  faltaMetaCompartilhamentos=metaCompartilhamentos-qtdeCompartilhamento;

  if qtdeCompartilhamento >= metaCompartilhamentos:
    print('Meta de Compartilhamentos do vídeo do Youtube alcançada com sucesso!')
    bateuMetaCompartilhamentos=1

  else: 
    print('Meta de Compartilhamentos do vídeo do Youtube ainda não alcançada. Ainda faltam ', faltaMetaCompartilhamentos, ' novos Compartilhamentos'  )
    bateuMetaCompartilhamentos=0
  return bateuMetaCompartilhamentos

def verificaRepositoriosGitHub(qtdeRepositorios):
  metaRepositorios = int (input ('Qual é a meta de Repositórios?  '))
  faltametaRepositorios=metaRepositorios-qtdeRepositorios;

  if qtdeRepositorios >= metaRepositorios:
    print('Meta de Repositórios presentes no GitHub alcançada com sucesso! ')
    bateumetaRepositorios=1

  else: 
    print('Meta de Repositórios ainda não alcançada. Ainda faltam ', faltametaRepositorios, ' novos Repositórios'  )
    bateumetaRepositorios=0
  return bateumetaRepositorios

def verificametas(bateuMetaInscritosYoutube, bateuMetaLikeVideoYoutube, bateuMetaCompartilhamentos, bateumetaRepositorios):
  if bateuMetaInscritosYoutube==1 and bateuMetaLikeVideoYoutube==1 and bateuMetaCompartilhamentos==1 and bateumetaRepositorios==1:
    print('Todas as metas foram alcançadas!')
    print ('Teremos bônus extra hoje!')
  else:
    print ('Não batemos todas as metas, infelizmente não teremos bônus extra hoje')

print('***********************************')
print ('Metas de inscritos no Canal do Youtube')
qtdeInscritosCanal = int (input ('Quantos inscritos temos no nosso do Canal Hoje?  '))
verificaMetaInscritosYoutube=metaInscritosCanalYoutube(qtdeInscritosCanal)

print('***********************************')
print ('Metas de Like no vídeo do Youtube')
qtdeLikeVideo = int (input ('Quantos Likes tivemos no nosso Vídeo?  '))
verificaLikesVideoYoutube=verificaLikesVideoYoutube(qtdeLikeVideo)

print ('************************************')
print ('Metas de Compartilhamento do Vídeo do Youtube')
qtdeCompartilhamento = int (input ('Quantos Compartilhamentos tivemos do nosso Vídeo?  '))
verificaCompartilhamento=verificaCompartilhamento(qtdeCompartilhamento)

print ('************************************')
print ('Metas de Repositórios presentes na Plataforma GitHub')
qtderepositorios = int (input ('Quantos Repositórios foram encontrados na Plataforma GitHub?  '))
verificaRepositoriosGitHub=verificaRepositoriosGitHub(qtderepositorios)

verificametas(verificaMetaInscritosYoutube, verificaLikesVideoYoutube, verificaCompartilhamento, verificaRepositoriosGitHub)
   

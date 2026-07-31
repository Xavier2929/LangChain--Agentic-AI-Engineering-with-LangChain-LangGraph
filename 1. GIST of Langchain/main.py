from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
load_dotenv()
def main():
    information = """
        Garry Kímovich Kaspárov (Bakú, 13 de abril de 1963) es un gran maestro de ajedrez, político y escritor ruso, que obtuvo la nacionalidad croata en 2014. Fue decimotercer campeón del mundo de ajedrez de 1985 a 1993, y campeón mundial versión PCA de 1993 a 2000. Es considerado uno de los mejores jugadores de todos los tiempos.

        Kaspárov se convirtió en el campeón del Mundo más joven de la historia en 1985. Mantuvo el título mundial oficial de la Federación Internacional de Ajedrez (FIDE) hasta 1993, cuando una disputa con la Federación lo llevó a crear una organización rival, la Professional Chess Association. Continuó manteniendo el Campeonato del Mundo de Ajedrez Clásico, hasta su derrota frente a Vladímir Krámnik en 2000.

        Kaspárov ha encabezado la clasificación mundial de la FIDE de forma casi continua desde 1986 hasta su retirada en 2005, alcanzando en julio de 1999 una puntuación de 2851, la mayor obtenida hasta el logro del GM Magnus Carlsen en mayo, al alcanzar este los 2882 puntos Elo. Además ha ganado en once ocasiones el Óscar del Ajedrez. También es conocido por sus enfrentamientos con computadoras y programas de ajedrez, especialmente tras su derrota en 1997 ante Deep Blue; esta fue la primera vez que una computadora derrotó a un Campeón del mundo en una partida con ritmo de juego de torneo.

        Kaspárov anunció su retirada del ajedrez profesional el 10 de marzo de 2005 para dedicar su tiempo a la política y a la escritura sobre temas de ajedrez. Formó el movimiento Frente Cívico Unido y se unió como miembro de La Otra Rusia, una coalición opositora a la administración de Vladímir Putin.

        El 28 de septiembre de 2007, Kaspárov entró en la carrera presidencial de Rusia, recibiendo 379 de 498 votos en un congreso celebrado en Moscú por La Otra Rusia.[4] Aunque finalmente su partido no concurrió a las elecciones de marzo de 2008, debido, según el propio Kaspárov, a la imposibilidad de conseguir un local lo suficientemente grande como para albergar al número de simpatizantes legalmente requeridos para respaldar su candidatura. Kasparov culpó a "la obstrucción oficial" por la falta de espacio disponible.[5][6]

        Kaspárov fue galardonado con el premio de la ONG UN Watch, por su pacífica lucha por el respeto de las libertades fundamentales en Rusia.[7] Actualmente es presidente de la Fundación de Derechos Humanos y preside su Consejo Internacional.
            """
    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary.
    2. two interesting facts about them.
    """
    prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-5"
    )
    chain = prompt_template | llm 
    response = chain.invoke(input={"information":information})
    print(response.content)
    



if __name__ == "__main__":
    main()

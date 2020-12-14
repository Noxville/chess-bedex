import asyncio
import chess
import chess.engine
import uuid
from models import GameState, ResultEvent
from publisher import RMQPublisher


async def main() -> None:
    while True:
        transport, engine = await chess.engine.popen_uci("/usr/games/stockfish")
        pub = RMQPublisher(game_id=str(uuid.uuid4()))
        board = chess.Board()
        pub.send(GameState(0, 'WHITE', None, board.fen()))
        while not board.is_game_over():
            result = await engine.play(board, chess.engine.Limit(time=5))
            board.push(result.move)
            pub.send(GameState(board.ply(), 'WHITE' if board.turn else 'BLACK', result.move.uci(), board.fen()))

        await engine.quit()
        pub.send(ResultEvent(board.result()))


asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())

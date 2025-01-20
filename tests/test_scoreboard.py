from sportradar.scoreboard import ScoreBoard

def test_create_empty_scoreboard():
    """Test if empty score board has no matches"""
    board = ScoreBoard()
    assert board.summary == []

def test_add_new_match_to_scoreboard():
    """Test if new match is added"""
    board = ScoreBoard()

    board.add("Mexico", "Brazil")

    assert len(board.summary) == 1

def test_score_is_zero_zero_for_new_matches():
    """Test if the match initial score is 0-0"""
    board = ScoreBoard()

    board.add("Mexico", "Brazil")

    first_match, = board.summary
    assert first_match.score == (0, 0)

def test_update_score():
    """Test if score of the match is updated"""
    board = ScoreBoard()

    match_id = board.add("Mexico", "Brazil")
    board.update_score(match_id, 1, 0)

    first_match, = board.summary
    assert first_match.score == (1, 0)

def test_remove_match():
    """Test if removed match is not in summary"""
    board = ScoreBoard()
    match_id =  board.add("Mexico", "Brazil")

    board.remove(match_id)

    assert board.summary == []



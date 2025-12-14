from api.BoardApi import BoardApi
import pytest


# def test_get_boards(api_client: BoardApi):
#     board_list = (api_client
#                   .get_all_boards_by_org_id("693af6e768691aeb25aa9f32"))
#     print(board_list)
#     # assert len(board_list.get("boards")) == 0

@pytest.mark.skip
def test_create_board(api_client: BoardApi):
    board_list_before = (api_client
                         .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
                         .get("boards"))

    api_client.create_board("Test Board")

    board_list_after = (api_client
                        .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
                        .get("boards"))

    assert len(board_list_after) - len(board_list_before == 1)


@pytest.mark.skip
def test_delete_board(api_client: BoardApi):
    board_list_before = (api_client
                         .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
                         .get("boards"))
    resp = api_client.delete_board_by_id("id")
    print(resp)
    board_list_after = (api_client
                        .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
                        .get("boards"))
    assert len(board_list_before) - len(board_list_after) == 1

# второй вариант удаления (через доп.фикстуру)
# def test_delete_board(api_client: BoardApi, dummy_board_id: str):
#     board_list_before = (api_client
#                          .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
#                          .get("boards"))
#     resp = api_client.delete_board_by_id("dummy_board_id")
#     print(resp)
#     board_list_after = (api_client
#                         .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
#                         .get("boards"))
#     assert len(board_list_before) - len(board_list_after) == 1


# второй вариант создания (сразу удаление)
# def test_create_board(api_client: BoardApi, delete_board: dict):
#     board_list_before = (api_client
#                          .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
#                          .get("boards"))

#     resp = api_client.create_board("New Board to be deleted")

#     delete_board["board_id"] = resp.get("id")

#     board_list_after = (api_client
#                         .get_all_boards_by_org_id("693af6e768691aeb25aa9f32")
#                         .get("boards"))

#     assert len(board_list_after) - len(board_list_before == 1)

import unittest
import src
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os



class TestLexSkeletonMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../LexingTestFiles/")

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testLexWholeFile(self):
        file = src.get_string_to_parse(self.filepath_prefix + "SkeletonMain.brs")
        result = self.lexer.lex(file)
        self.assertEqual(result["Status"], 'Success')

    def testLexWholeFileWithMultipleErrors(self):
        file = src.get_string_to_parse(self.filepath_prefix + "SkeletonMainWithErrors.brs")
        result = self.lexer.lex(file)
        exp_result = [self.error.get(ErrConst.UNMATCHED_QUOTATION_MARK, ['"roSGScreen', 2]),
                      self.error.get(ErrConst.UNMATCHED_QUOTATION_MARK, ['"SampleScene', 6])]
        self.assertEqual(result["Tokens"], exp_result)
        self.assertEqual(result["Status"], 'Error')
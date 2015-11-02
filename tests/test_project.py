'''
Created on 2nd Nov 2015

@author: hutcheb
'''
import unittest, l5x

class TagTestCase(unittest.TestCase):

    def setUp(self):
        self.prj = l5x.Project('basetest.L5X')       
                     
    def tearDown(self):        
        pass
    
    def test_OpenProject(self):
        """Confirm test l5x file can be opened"""
        self.assertTrue(self.prj != None) 
     
    def test_ConfirmBooleanTag(self):
        """Confirm boolean1 tag exists and is correct"""  
        description = 'Test Boolean 1'
        tag = 'boolean1'
        data_type = 'BOOL'   
        external_access = 'Read/Write'
        constant = "false"
        
        ctl_tags = self.prj.controller.tags
        tag_names = ctl_tags.names                
        self.assertTrue(tag in tag_names)        
        self.assertEqual(ctl_tags[tag].data_type, data_type)            
        self.assertEqual(ctl_tags[tag].description, description)     
        self.assertEqual(ctl_tags[tag].external_access, external_access) 
        
    def test_ConfirmRealTag(self):
        """Confirm real1 tag exists and is correct"""  
        description = 'Test Real 1'
        tag = 'real1'
        data_type = 'REAL'   
        external_access = 'Read/Write'
        constant = "false"     
        
        ctl_tags = self.prj.controller.tags
        tag_names = ctl_tags.names                
        self.assertTrue(tag in tag_names)        
        self.assertEqual(ctl_tags[tag].data_type, data_type)            
        self.assertEqual(ctl_tags[tag].description, description)     
        self.assertEqual(ctl_tags[tag].external_access, external_access) 
        self.assertEqual(ctl_tags[tag].constant, constant) 

    def test_ConfirmDintTag(self):
        """Confirm DINT1 tag exists and is correct"""  
        description = 'Test DINT 1'
        tag = 'dint1'
        data_type = 'DINT'   
        external_access = 'Read/Write'
        constant = "false"     
        
        ctl_tags = self.prj.controller.tags
        tag_names = ctl_tags.names                
        self.assertTrue(tag in tag_names)        
        self.assertEqual(ctl_tags[tag].data_type, data_type)            
        self.assertEqual(ctl_tags[tag].description, description)     
        self.assertEqual(ctl_tags[tag].external_access, external_access) 
        self.assertEqual(ctl_tags[tag].constant, constant) 
        
    def test_ConfirmProgram(self):
        """Confirm MainProgram gets created"""  
        name = 'MainProgram' 
        test_edits = "false"
        main_routine_name = "MainRoutine"
        disabled = "false"
             
        self.assertTrue(name in self.prj.programs.names)  
        prog = self.prj.programs[name]
        self.assertEqual(prog.test_edits, test_edits) 
        self.assertEqual(prog.main_routine_name, main_routine_name) 
        self.assertEqual(prog.disabled, disabled) 
    
    def test_ConfirmRoutine(self):
        """Confirm MainRoutine gets created"""  
        program = 'MainProgram'        
        name = 'MainRoutine'   
        type = "RLL"
              
        self.assertTrue(name in self.prj.programs[program].routines.names)  
        routine = self.prj.programs[program].routines[name]
        self.assertEqual(routine.type, type)


    def test_ConfirmProgramTag(self):
        """Confirm boolean2 tag exists and is correct"""  
        description = 'Test Boolean 2'
        tag = 'boolean2'
        data_type = 'BOOL'   
        external_access = 'Read/Write'
        constant = "false"
        program = 'MainProgram'   
        
        prog_tags = self.prj.programs[program].tags
        tag_names = prog_tags.names                
        self.assertTrue(tag in tag_names)        
        self.assertEqual(prog_tags[tag].data_type, data_type)            
        self.assertEqual(prog_tags[tag].description, description)     
        self.assertEqual(prog_tags[tag].external_access, external_access) 
        self.assertEqual(prog_tags[tag].constant, constant) 

       
if __name__ == "__main__": 
    unittest.main()
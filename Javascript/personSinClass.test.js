import darNombreAPersona from "personSinClass.js"

describe("Describe persona", () => {
    it("dar nombre a persona", () => {
      // Arrange
      const nombre = 'Elena'
  
      // Action to test
      const action = darNombreAPersona(nombre)
  
      // Assert
      expect(action).toBe('Elena')
    })
  })
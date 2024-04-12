import { Person } from "person.js"

describe('Person Suite', () => {
    it('Create Person', () => {
        const p1 = new Person()
        p1.setName('Ana')
        p1.getName()

        expect(name).toEqual('Ana')

    })

})